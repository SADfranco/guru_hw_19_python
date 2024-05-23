import os
import allure
import requests


def attach_bstack_video(session_id):

    import requests
    bstack_session = requests.get(
        f'{os.getenv("BROWSERSTACK_API_SESSIONS")}/{session_id}.json',
        auth=(os.getenv("BROWSERSTACK_LOGIN"), os.getenv("BROWSERSTACK_PASS")),
    ).json()
    print(bstack_session)
    video_url = bstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML,
    )
