import re
import webbrowser
# import requests
# from bs4 import BeautifulSoup


def get_download_links(model_urls):
    download_urls = []
    for url in model_urls:
        if not url.startswith('https://www.models-resource.com/'):
            continue
        model_id = get_id(url)
        download_urls.append(f"https://www.models-resource.com/download/{model_id}/")

    return download_urls


def get_id(mdl_url):
    pattern = r'/(\d+)/$'
    match = re.search(pattern, mdl_url)
    if match:
        return match.group(1)
    else:
        print('No match found.')


def download_models(model_urls):
    model_urls = get_download_links(model_urls)
    for link in model_urls:
            webbrowser.open(link)

# TODO: Download files without having to open the browser
# r = requests.get(link)
# file_name = link.split("/")[-1]
# with open(file_name, "wb") as f:
#     f.write(r.content)
