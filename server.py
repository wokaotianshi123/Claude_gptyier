import web
import requests
import jsonpath
import json
import random
import time
import html


urls = (
    '/gptyier', 'gptyier',
    '/setsession', 'setsession',
    '/stream', 'stream',
    '/css/(.*)', 'static_handler_css',
    '/js/(.*)', 'static_handler_js',
)

headers = {
        'Host': '139wokao.slack.com',
        'Cookie': 'b=97cf412a5913ef6babd6e2d49526317a; _gcl_au=1.1.350294721.1689900899; OptanonAlertBoxClosed=2023-07-21T01:05:01.705Z; _lc2_fpi=e00b11ac9c9b--01h5tznba97gm4qfcace6wjt4s; _cs_c=1; d=xoxd-iM9msWLuwQXUkNcO3jc5v%2BxWqAQVoMsq694hWsOIRmeGSZjHGBjU7EX%2FVZFnpZUg5aPQZ17N6UzsklUoViepJzPaiz9DC0coGG8KhdAyv%2FKqUGopgCxD2oyshXy45%2BKcmEcf3SxJ6VpdzfO2w2GXE5RMbkvTtG9OtszUwDPmtJWS24Pc3A1ZZtnsdQ%3D%3D; lc=1689901519; tz=480; d-s=1690169834; x=97cf412a5913ef6babd6e2d49526317a.1690169834; _cs_mk_ga=0.6672402806626914_1690169840452; DriftPlaybook=B; _ga_QTJQME5M5D=GS1.1.1690169840.2.0.1690169840.60.0.0; _ga=GA1.2.165405858.1689901509; _gid=GA1.2.1010259680.1690169841; _cs_cvars=%7B%221%22%3A%5B%22Visitor%20ID%22%2C%2297cf412a5913ef6babd6e2d49526317a%22%5D%2C%222%22%3A%5B%22Is%20Signed%20In%22%2C%22true%22%5D%2C%223%22%3A%5B%22URL%20Path%22%2C%22%2Fintl%2Fzh-cn%2F%22%5D%2C%224%22%3A%5B%22Visitor%20Type%22%2C%22prospect%22%5D%7D; _cs_id=a46bce8e-3f15-a79a-cff6-d714ee0b3077.1689901510.2.1690169841.1690169841.1.1724065510294; _cs_s=1.0.0.1690171641982; _li_dcdm_c=.slack.com; __adroll_fpc=afd56902a678be4de8158818eb468875-1690169855403; __qca=P0-156302808-1690169841266; shown_ssb_redirect_page=1; __ar_v4=%7C4UHU5P4P3FESHLUMNBLWAU%3A20230723%3A1%7CQCM34G7NBZEHHATIFDIUBJ%3A20230723%3A1%7CK2HN2U4VSJGOVKC2WJLQNH%3A20230723%3A1; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Jul+24+2023+11%3A39%3A19+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202211.1.0&isIABGlobal=false&hosts=&consentId=f029ca60-b6cf-42dc-8942-fef002ae79dc&interactionCount=2&landingPath=NotLandingPage&groups=1%3A1%2C2%3A1%2C3%3A1%2C4%3A1&geolocation=CN%3BSC&AwaitingReconsent=false; shown_download_ssb_modal=1; show_download_ssb_banner=1; no_download_ssb_banner=1',
    }

token="xoxc-5586135847479-5613310679857-5638833143200-55aa0a1d75aa01e2b3ff00505c5789c5a232307a782f430f15d3cd1725a696a4"

Claude_userid="U05J194KZR7"
fangjian_id="D05HR3W314L"

app = web.application(urls, globals())
app.debug = False
render = web.template.render('templates')


class gptyier:
    def GET(self):
        web.header('Content-Type', 'text/html; charset=utf-8')
        with open('gpt.html', 'r',encoding='utf-8') as file:
            html_content = file.read()
        return html_content



class static_handler_css:
    def GET(self, filename):
        try:
            with open(f'css/{filename}', 'rb') as f:
                return f.read()
        except FileNotFoundError:
            raise web.notfound("File not found")
class static_handler_js:
    def GET(self, filename):
        try:
            with open(f'js/{filename}', 'rb') as f:
                return f.read()
        except FileNotFoundError:
            raise web.notfound("File not found")

class setsession:

    def POST(self):

        stream_url_post_postMessage_r_json_ts = web.cookies().get('ts')
        url_conversations_replies_huoqu_latest_reply_json_latest_reply2 = web.cookies().get('latest_reply')


        setsession_data = web.input(message=None)
        message = setsession_data.message


        message=message.replace("\"", '\\\"')

        print(message)

        prompt=message


        url_post_postMessage = 'https://139wokao.slack.com/api/chat.postMessage'

        if(url_conversations_replies_huoqu_latest_reply_json_latest_reply2!=None):
            url_post_postMessage_file = {
                'token': (None,
                          token,
                          None),
                'channel': (None, '{}'.format(fangjian_id), None),
                'ts': (None, '1681546073.xxxxx5', None),
                'type': (None, 'message', None),
                'reply_broadcast': (None, 'false', None),
                'thread_ts': (None, '{}'.format(stream_url_post_postMessage_r_json_ts), None),
                'unfurl': (None, '[]', None),
                'blocks': (None,
                           '[{"type":"rich_text","elements":[{"type":"rich_text_section","elements":[{"type":"user","user_id":"%s"},{"type":"text","text":" %s"}]}]}]' % (
                               Claude_userid,prompt), None),
                'include_channel_perm_error': (None, 'true', None),
                '_x_reason': (None, 'webapp_message_send', None),
                '_x_mode': (None, 'online', None),
                '_x_sonic': (None, 'true', None)
            }
        else:
            url_post_postMessage_file = {
                'token': (None,
                          token,
                          None),
                'channel': (None, '{}'.format(fangjian_id), None),
                'ts': (None, '1681546073.xxxxx5', None),
                'type': (None, 'message', None),
                'unfurl': (None, '[]', None),
                'blocks': (None,
                           '[{"type":"rich_text","elements":[{"type":"rich_text_section","elements":[{"type":"user","user_id":"%s"},{"type":"text","text":" %s"}]}]}]' % (
                               Claude_userid,prompt), None),
                'include_channel_perm_error': (None, 'true', None),
                '_x_reason': (None, 'webapp_message_send', None),
                '_x_mode': (None, 'online', None),
                '_x_sonic': (None, 'true', None)
            }

        try:
            url_post_postMessage_r = requests.post(url_post_postMessage, headers=headers,
                                               files=url_post_postMessage_file, verify=False)

        except BaseException as e:
            print("查询失败,正在重试")
            print(e)
            for o in range(100):
                try:
                    url_post_postMessage_r = requests.post(url_post_postMessage, headers=headers,
                                                           files=url_post_postMessage_file, verify=False)
                    if url_post_postMessage_r.status_code == 200:
                        break
                except BaseException as e:
                    print("再次查询子域名失败", o)
                    print(e)

        if ("\"ok\":true" in url_post_postMessage_r.text and "thread_ts" in url_post_postMessage_r.text and url_conversations_replies_huoqu_latest_reply_json_latest_reply2!=None):
            url_post_postMessage_r_json = json.loads(url_post_postMessage_r.text)
            url_post_postMessage_r_json_thread_ts = jsonpath.jsonpath(url_post_postMessage_r_json, "$.message.thread_ts")[0]

            url_post_postMessage_r_json_ts = jsonpath.jsonpath(url_post_postMessage_r_json, "$.ts")[0]
            web.setcookie('ts', '{}'.format(url_post_postMessage_r_json_thread_ts), 36000)
            web.setcookie('thread_ts', '{}'.format(url_post_postMessage_r_json_ts), 36000)


            return '{"success":true}'
        elif ("\"ok\":true" in url_post_postMessage_r.text and url_conversations_replies_huoqu_latest_reply_json_latest_reply2==None):
            url_post_postMessage_r_json = json.loads(url_post_postMessage_r.text)
            url_post_postMessage_r_json_ts = jsonpath.jsonpath(url_post_postMessage_r_json, "$.ts")[0]
            web.setcookie('ts', '{}'.format(url_post_postMessage_r_json_ts), 36000)

            return '{"success":true}'
        else:
            return '{"success":false}'


class stream:
    def GET(self):

        stream_url_post_postMessage_r_json_ts = web.cookies().get('ts')
        # url_conversations_replies_huoqu_latest_reply_json_latest_reply2 = web.cookies().get('latest_reply')
        url_post_postMessage_r_json_thread_ts = web.cookies().get('thread_ts')

        url_conversations_replies = 'https://139wokao.slack.com/api/conversations.replies'


        for i in range(120):
            try:
                url_conversations_replies_file = {
                    'token': (None,
                              token,
                              None),
                    'channel': (None, '{}'.format(fangjian_id), None),
                    'ts': (None, '{}'.format(stream_url_post_postMessage_r_json_ts), None),
                    'inclusive': (None, 'ture', None),
                    'limit': (None, '28', None),
                    'oldest': (None, '{}'.format(stream_url_post_postMessage_r_json_ts), None),
                    '_x_reason': (None, 'history-api/fetchReplies', None),
                    '_x_mode': (None, 'online', None),
                    '_x_sonic': (None, 'true', None)
                }
                url_conversations_replies_huoqu_latest_reply = requests.post(url_conversations_replies, headers=headers,
                                                        files=url_conversations_replies_file, verify=False)
            except BaseException as e:
                print("查询失败,正在重试")
                print(e)
                for o in range(100):
                    try:
                        url_conversations_replies_huoqu_latest_reply = requests.post(url_conversations_replies, headers=headers,
                                                                    files=url_conversations_replies_file,
                                                                    verify=False)
                        if url_conversations_replies_huoqu_latest_reply.status_code == 200:
                            break
                    except BaseException as e:
                        print("再次查询子域名失败", o)
                        print(e)

            if(i>2 and "latest_reply" not in url_conversations_replies_huoqu_latest_reply.text and "thread_ts" not in url_conversations_replies_huoqu_latest_reply.text):
                web.header('Content-Type', 'text/event-stream')
                web.header('Access-Control-Allow-Origin', '*')
                web.header('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
                web.header('Pragma', 'no-cache')
                return """data: {"id":"chatcmpl-75nIQFpIpwE3zjcpga0VGgULV3Lyh","object":"chat.completion.chunk","created":1681615490,"model":"gpt-3.5-turbo-0301","choices":[{"delta":{"content":"%s"},"index":0,"finish_reason":null}]}


                            data: [DONE]

                            """ % ("错误")

            #print(url_conversations_replies_huoqu_latest_reply.text)
            if ("\"ok\":true" in url_conversations_replies_huoqu_latest_reply.text and "latest_reply" in url_conversations_replies_huoqu_latest_reply.text and "thread_ts" in url_conversations_replies_huoqu_latest_reply.text):

                url_conversations_replies_huoqu_latest_reply_json = json.loads(url_conversations_replies_huoqu_latest_reply.text)

                url_conversations_replies_huoqu_latest_reply_json_messages_latest_reply = jsonpath.jsonpath(url_conversations_replies_huoqu_latest_reply_json, "$.messages[0].latest_reply")[0]

                #print("url_conversations_replies_huoqu_latest_reply_json_messages_latest_reply:{}".format(url_conversations_replies_huoqu_latest_reply_json_messages_latest_reply))
                #print("url_post_postMessage_r_json_thread_ts:{}".format(url_post_postMessage_r_json_thread_ts))

                if(url_post_postMessage_r_json_thread_ts!=url_conversations_replies_huoqu_latest_reply_json_messages_latest_reply and url_post_postMessage_r_json_thread_ts!=None):
                    #print(url_conversations_replies_huoqu_latest_reply_json_messages_latest_reply)
                    web.setcookie('latest_reply', '{}'.format(url_conversations_replies_huoqu_latest_reply_json_messages_latest_reply), 36000)
                    break

                elif(url_post_postMessage_r_json_thread_ts==None):
                    #print(url_post_postMessage_r_json_thread_ts)
                    web.setcookie('latest_reply',
                                  '{}'.format(url_conversations_replies_huoqu_latest_reply_json_messages_latest_reply),
                                  36000)
                    break
            else:
                time.sleep(0.2)
        # url_conversations_replies_huoqu_latest_reply_json_messages_latest_reply = web.cookies().get('latest_reply')


        if(url_conversations_replies_huoqu_latest_reply_json_messages_latest_reply!=None):
            for i in range(120):
                try:
                    url_conversations_replies_file2 = {
                        'token': (None,
                                  token,
                                  None),
                        'channel': (None, '{}'.format(fangjian_id), None),
                        'ts': (None, '{}'.format(url_conversations_replies_huoqu_latest_reply_json_messages_latest_reply), None),
                        'inclusive': (None, 'ture', None),
                        'limit': (None, '28', None),
                        'oldest': (None, '{}'.format(url_conversations_replies_huoqu_latest_reply_json_messages_latest_reply), None),
                        '_x_reason': (None, 'history-api/fetchReplies', None),
                        '_x_mode': (None, 'online', None),
                        '_x_sonic': (None, 'true', None)
                    }
                    url_conversations_replies_r = requests.post(url_conversations_replies, headers=headers,
                                                            files=url_conversations_replies_file2, verify=False)
                except BaseException as e:
                    print("查询失败,正在重试")
                    print(e)
                    for o in range(100):
                        try:
                            url_conversations_replies_r = requests.post(url_conversations_replies, headers=headers,
                                                                        files=url_conversations_replies_file2,
                                                                        verify=False)
                            if url_conversations_replies_r.status_code == 200:
                                break
                        except BaseException as e:
                            print("再次查询子域名失败", o)
                            print(e)

                # print(url_conversations_replies_r.text)
                if(i>2 and "_Typing" not in url_conversations_replies_r.text and "thread_ts" not in url_conversations_replies_r.text):
                    web.header('Content-Type', 'text/event-stream')
                    web.header('Access-Control-Allow-Origin', '*')
                    web.header('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
                    web.header('Pragma', 'no-cache')
                    return """data: {"id":"chatcmpl-75nIQFpIpwE3zjcpga0VGgULV3Lyh","object":"chat.completion.chunk","created":1681615490,"model":"gpt-3.5-turbo-0301","choices":[{"delta":{"content":"%s"},"index":0,"finish_reason":null}]}\n\n\ndata: [DONE]\n\n"""% ("错误")

                if ("\"ok\":true" in url_conversations_replies_r.text and "_Typing" not in url_conversations_replies_r.text and "thread_ts" in url_conversations_replies_r.text):
                    url_conversations_replies_r_json = json.loads(url_conversations_replies_r.text)
                    url_conversations_replies_r_json_text = jsonpath.jsonpath(url_conversations_replies_r_json, "$.messages[0].text")[0]

                    url_conversations_replies_r_json_text=html.unescape(url_conversations_replies_r_json_text).replace("\n","\\\\n").replace("\"","\\\"")

                    break
                else:
                    time.sleep(1)
            else:
                web.header('Content-Type', 'text/event-stream')
                web.header('Access-Control-Allow-Origin', '*')
                web.header('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
                web.header('Pragma', 'no-cache')
                return """data: {"id":"chatcmpl-75nIQFpIpwE3zjcpga0VGgULV3Lyh","object":"chat.completion.chunk","created":1681615490,"model":"gpt-3.5-turbo-0301","choices":[{"delta":{"content":"%s"},"index":0,"finish_reason":null}]}\n\n\ndata: [DONE]\n\n"""% ("错误")

            #print(url_conversations_replies_r_json_text)
            web.header('Content-Type', 'text/event-stream')
            web.header('Access-Control-Allow-Origin', '*')
            web.header('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
            web.header('Pragma', 'no-cache')
            return """data: {"id":"chatcmpl-75nIQFpIpwE3zjcpga0VGgULV3Lyh","object":"chat.completion.chunk","created":1681615490,"model":"gpt-3.5-turbo-0301","choices":[{"delta":{"content":"%s"},"index":0,"finish_reason":null}]}\n\n\ndata: [DONE]\n\n"""%(url_conversations_replies_r_json_text)


if __name__ == "__main__":
    app.run()
