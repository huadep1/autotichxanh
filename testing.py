import requests

cookies = {
    "sb": "o8ufZMHpHElk60IJDkE7NT8g",
    "datr": "UYvGZIURBYggF4vXPAAsE_EW",
    "c_user": "100064051429806",
    "xs": "37%3A7Eg_R5ocLoZWog%3A2%3A1690733437%3A-1%3A14488%3A%3AAcU4g7hqYK9sB3IWV7W5PeZCnvxF1JTJqESewNZS8Ek",
    "fr": "0eoGD8VfpUc8lYQuH.AWWpMzGhsA379u7AtVGF4MdHbrs.Bk6drK.ue.AAA.0.0.Bk6drK.AWVcYxw4qYc",
    "wd": "496x823",
}

headers = {
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
}

data = {
    "Field176493164581449": "Driver's License",
    "Field206407204842001": "AZWAd4E-UDz7dl0YN3yEd-TndZVOuQMG0J59v4Ls2IwHSxjEI05UixrWyEReJtlbQ3bV1AdBNPvYkcnhR9pl-Ysfo6rCMKyfnww0LC9sI2yE5NMuA6v0QZq6Qx_Va_3A69-_uzIzNY2qYixZFL-9M01dl0v9pS3fOdzPCJMdkTNWbO6xTFj87ItbBwqQ1YQcGPyT2OK5_PjfR3OM0MPV1tRa3WuFgC7YKyi9EhZFHr0R_EA6JrBBIicP1XjjhjIpWAI4W6h8Dv-GHLt8y9sAkb281Xsg8dhIR-gUVm8I7rw5I2IojecMxBbjc5a7WCBofIZXw76cMo77SsnZl1rVN3zkRxmv0JG8-Tkwyvk0N2w0Gwh3JKBrBnVT_-cyNPK1d5MIaMXozeaDPJQoQWycnJvvFZHXii24vj72Ht7fwRiU3A",
    "__a": "1",
    "abuse_agreement[0]": "agree",
    "additional_comments": "Test",
    "audience": "Audience",
    "category": "News/Media",
    "country": "United States",
    "country_iso2_country_code": "US",
    "dpr": "1",
    "fb_dtsg": "NAcOWKQoudZlufxYfy0lo00c3s90fIB0yqww1YvZHC68GJRyllrFgDg:37:1690733437",
    "fbid": "https://www.facebook.com/emfbroadcasting",
    "jazoest": "25597",
    "mediaopsbot_token": "",
    "notability_links_1": "",
    "notability_links_2": "",
    "notability_links_3": "",
    "notability_links_4": "",
    "notability_links_5": "",
    "other_names": "Also known as",
    "parent_job_id": "",
    "platform": "FB",
    "priority": "LOW",
    "support_form_fact_false_fields": "[]",
    "support_form_hidden_fields": "{}",
    "support_form_id": "629393694645076",
    "support_form_locale_id": "en_GB",
}

response = requests.post(
    "https://httpbin.org/post",
    headers=headers,
    data=data,
)
print(response.text)
