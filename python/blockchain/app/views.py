import datetime
import json

import requests
from flask import render_template, redirect, request

from app import app

CONNECTED_NODE_ADDRESS = "http://127.0.0.1:8000"

posts = []


def fetch_posts():
    """
    从区块链节点获取链，解析后存储在本地。
    """
    get_chain_address = "{}/chain".format(CONNECTED_NODE_ADDRESS)
    print(get_chain_address)

    response = requests.get(get_chain_address)
    if response.status_code == 200:
        content = []
        chain = json.loads(response.content)
        for block in chain["chain"]:
            for tx in block["transactions"]:
                tx["index"] = block["index"]
                tx["hash"] = block["previous_hash"]
                content.append(tx)

        global posts
        posts = sorted(content, key=lambda k: k['timestamp'], reverse=True)


@app.route('/')
def index():
    print(" ====== index start ======")
    
    fetch_posts()
    return render_template('index.html',
                           title='去中心化内容分享',
                           posts=posts,
                           node_address=CONNECTED_NODE_ADDRESS,
                           readable_time=timestamp_to_string)


@app.route('/submit', methods=['POST'])
def submit_textarea():
    print(" ====== submit_textarea start ======")

    """
    创建新事务
    """
    post_content = request.form["content"]
    author = request.form["author"]

    post_object = {
        'author': author,
        'content': post_content,
    }

    # 提交事务
    new_tx_address = "{}/new_transaction".format(CONNECTED_NODE_ADDRESS)

    print(new_tx_address)
    print(author)
    print(post_content)
    print(post_object)

    requests.post(new_tx_address,
                  json=post_object,
                  headers={'Content-type': 'application/json'})

    return redirect('/')


def timestamp_to_string(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time).strftime('%H:%M')
