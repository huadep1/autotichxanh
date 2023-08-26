import asyncio
import json
import re

import aiohttp


async def getsession(
    ses: aiohttp.ClientSession, cookies: dict[str, str], data: dict[str, str]
) -> None:
    async with ses.get(
        "https://www.facebook.com/help/contact/629393694645076",
        cookies=cookies,
        headers={
            "authority": "www.facebook.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "en-US,en;q=0.9,vi;q=0.8",
            "cache-control": "max-age=0",
            "dpr": "1",
            "sec-ch-prefers-color-scheme": "dark",
            "sec-ch-ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            "sec-ch-ua-full-version-list": '"Chromium";v="116.0.5845.111", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.111"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-model": '""',
            "sec-ch-ua-platform": '"Windows"',
            "sec-ch-ua-platform-version": '"10.0.0"',
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
            "viewport-width": "496",
        },
    ) as response:
        response_body = await response.text()
        jazoest = re.search(r'name="jazoest" value="([^"]+)"', response_body).group(1)
        fb_dtsg = re.search(r'name="fb_dtsg" value="([^"]+)"', response_body).group(1)
        data["jazoest"] = jazoest
        data["fb_dtsg"] = fb_dtsg
        return await postsession(ses, cookies, data)


async def postsession(
    ses: aiohttp.ClientSession, cookies: dict[str, str], data: dict[str, str]
) -> str:
    async with ses.post(
        "https://www.facebook.com/ajax/help/contact/submit/page",
        data=data,
        headers={
            "authority": "www.facebook.com",
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9,vi;q=0.8",
            "content-type": "application/x-www-form-urlencoded",
            "dpr": "1",
            "origin": "https://www.facebook.com",
            "referer": "https://www.facebook.com/help/contact/629393694645076",
            "sec-ch-prefers-color-scheme": "dark",
            "sec-ch-ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            "sec-ch-ua-full-version-list": '"Chromium";v="116.0.5845.111", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.111"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-model": '""',
            "sec-ch-ua-platform": '"Windows"',
            "sec-ch-ua-platform-version": '"10.0.0"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
            "viewport-width": "496",
            "x-asbd-id": "129477",
            "x-fb-lsd": "kgCK9ixIPoOP39qxqvm7T1",
        },
        cookies=cookies,
    ) as response:
        return await response.text()


async def fetchsession(ses: aiohttp.ClientSession, cookiess: list[str]) -> None:
    data = {
        "Field176493164581449": "Driver's License",
        "Field206407204842001": "",
        "__a": "1",
        "abuse_agreement[0]": "agree",
        "additional_comments": "",
        "audience": "",
        "category": "News/Media",
        "country": "United States",
        "country_iso2_country_code": "US",
        "dpr": "1",
        "fb_dtsg": "",
        "fbid": "",
        "jazoest": "",
        "mediaopsbot_token": "",
        "notability_links_1": "",
        "notability_links_2": "",
        "notability_links_3": "",
        "notability_links_4": "",
        "notability_links_5": "",
        "other_names": "",
        "parent_job_id": "",
        "platform": "FB",
        "priority": "LOW",
        "support_form_fact_false_fields": "[]",
        "support_form_hidden_fields": "{}",
        "support_form_id": "629393694645076",
        "support_form_locale_id": "en_GB",
    }
    tasks = []
    for cookie in cookiess:
        cookies = {}
        for item in cookie.split(";"):
            item = item.strip()
            if not item:
                continue
            if "=" not in item:
                cookie[item] = None
                continue
            name, value = item.split("=", 1)
            cookies[name] = value
        task = asyncio.create_task(getsession(ses, cookies, data))
        tasks.append(task)
    res = await asyncio.gather(*tasks)
    return res


async def main():
    clone = open(r"listvia.txt", "r").read().split()
    while len(clone) > 0:
        clones = clone[:500]
        [clone.remove(i) for i in clones]
        print(len(clone))
        async with aiohttp.ClientSession() as ses:
            result = await fetchsession(ses, clones)
        print(result)


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
