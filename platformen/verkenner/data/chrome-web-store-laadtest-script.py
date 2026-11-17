from playwright.sync_api import sync_playwright
import sys
ext=__import__("sys").argv[1] if len(__import__("sys").argv)>1 else "ext"
with sync_playwright() as p:
    ctx=p.chromium.launch_persistent_context("",channel="chrome",headless=True,args=["--headless=new",f"--disable-extensions-except={ext}",f"--load-extension={ext}","--disable-features=DisableLoadExtensionCommandLineSwitch"])
    sw=ctx.service_workers or [ctx.wait_for_event("serviceworker",timeout=10000)]
    print("service worker:",sw[0].url)
    pg=ctx.new_page(); pg.set_content("<html><body>hi</body></html>"); pg.goto("data:text/html,<p>x</p>")
    pg.goto("https://example.com"); print("content script:",pg.evaluate("document.documentElement.dataset.ext"))
    print(ctx.browser and ctx.browser.version if ctx.browser else "", )
    ctx.close()
