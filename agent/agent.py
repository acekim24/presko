from aiohttp import web
import asyncio

async def handle_request_scan(request):
    try:
        data = await request.json()
        print(f"Received scan request: {data}")
        # Here you can add your actual scanning logic (local only, safe)
        return web.json_response(
            {"status": "ok", "message": "Scan started locally"},
            headers={
                "Access-Control-Allow-Origin": "https://YOUR_NETLIFY_SUBDOMAIN.netlify.app",
                "Access-Control-Allow-Methods": "POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            }
        )
    except Exception as e:
        print("Error:", e)
        return web.json_response({"status": "error", "error": str(e)}, status=500)

async def options_handler(request):
    """Handles preflight OPTIONS requests (CORS)."""
    return web.Response(
        status=204,
        headers={
            "Access-Control-Allow-Origin": "https://YOUR_NETLIFY_SUBDOMAIN.netlify.app",
            "Access-Control-Allow-Methods": "POST, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type"
        }
    )

def main():
    app = web.Application()
    app.router.add_post("/request-scan", handle_request_scan)
    app.router.add_options("/request-scan", options_handler)

    web.run_app(app, host="127.0.0.1", port=8765)

if __name__ == "__main__":
    print("✅ Local agent running at http://127.0.0.1:8765")
    asyncio.run(main())
