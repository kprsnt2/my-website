/**
 * Cloudflare Email Worker — Receives emails at interview@kprsnt.in
 * Parses the email, forwards it to the Vercel API for AI processing,
 * which then sends the reply via Resend.
 * 
 * Deploy via Cloudflare Dashboard → Workers & Pages → Create Worker
 * Then enable Email Routing → Route interview@kprsnt.in → this Worker
 */

import PostalMime from 'postal-mime';

export default {
  // Handle incoming emails via Cloudflare Email Routing
  async email(message, env, ctx) {
    try {
      // Parse the raw email
      const rawEmail = await streamToArrayBuffer(message.raw, message.rawSize);
      const parser = new PostalMime();
      const parsed = await parser.parse(rawEmail);

      const fromEmail = message.from;
      const subject = parsed.subject || 'Interview Question';
      // Prefer plain text, fall back to stripped HTML
      const body = parsed.text || parsed.html?.replace(/<[^>]*>/g, '') || '';

      if (!body.trim()) {
        console.log('Empty email body, skipping');
        return;
      }

      // Forward to Vercel API for AI processing + email reply
      const response = await fetch(env.VERCEL_API_URL || 'https://kprsnt.in/api/interview', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          message: body,
          from_email: fromEmail,
          subject: subject,
          send_email: true  // Tell the API to send a reply
        })
      });

      const result = await response.json();
      console.log(`Processed email from ${fromEmail}: email_sent=${result.email_sent}`);

    } catch (error) {
      console.error('Email processing error:', error);
    }
  },

  // Optional: HTTP endpoint for testing the worker
  async fetch(request, env) {
    if (request.method === 'GET') {
      return new Response(JSON.stringify({
        status: 'online',
        service: 'Cloudflare Email Worker for interview@kprsnt.in',
        description: 'This worker receives emails and forwards them to the AI interview bot.'
      }, null, 2), {
        headers: { 'Content-Type': 'application/json' }
      });
    }
    return new Response('Method not allowed', { status: 405 });
  }
};

// Helper: Convert ReadableStream to ArrayBuffer
async function streamToArrayBuffer(stream, streamSize) {
  let result = new Uint8Array(streamSize);
  let bytesRead = 0;
  const reader = stream.getReader();

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    result.set(value, bytesRead);
    bytesRead += value.length;
  }

  return result;
}
