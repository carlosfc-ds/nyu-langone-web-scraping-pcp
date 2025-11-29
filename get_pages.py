import requests
import json

page_numbers = [str(k) for k in range(1, 25)]

for page_number in page_numbers:
    url = f"https://nyulangone.org/api/providers?sort=availability&page={page_number}&original-criteria=treatment&treatment=primary-care&pageSize=20&timestamp=1763926568740"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        with open(f"pages/doctors_page{page_number}.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("JSON saved successfully.")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
