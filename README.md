#智能助手

唤醒模块：snowboy
    - 唤醒模块一旦唤醒暂时就不工作， 直到该次唤醒工作结束后再继续工作
    - 唤醒之后检查网络状态
        - 检查是否可以接入chatgpt
    - snowboy/或其他唤醒模块


录音模块：pyaudio
    - 10秒内没人说话就关闭
        - 系统继续进入等待唤醒状态
    - 讲话时间超过十秒：十秒之后如果唤醒人继续讲话，需要继续监听
        - 如果说话超过30秒，我们就暂停录音，否则进入下一步
    - 录制完成的音频，存储成wav, 或流处理方式完成tts处理
        - 录音完成后，录音模块不再工作


语音转文字：pythonstt/baidu
    - 使用python模块达到预期效果 （迅速）
    - 获取返回文字
        - 如果文字返回为空，提示重说一次
        - 根据出错提示做出相应反馈
            - 重说一次 - 进入录音
            - 网络错误 - 进入待唤醒状态

对话机器人：chatgpt
    - 提问模块： （extra - 接入chatgpt获取回复）
    - 根据命令实现电脑控制和数据查找
        - 电脑控制
        - 爬虫模块： 查找目标数据 (python)
    - 如果返回出错，处理方式同上
        

文字转语音tts：
    - 将返回文字转换成语音
    - 如果返回出错，处理方式同上
s

播放反馈：播放语音

主体控制模块：
    - 当对话机器人回应唤醒人的时候， 是否自动进入下一轮的录音/回应完成之后就进入待唤醒状态
    - 如果假如查找和电脑控制， 需要提供两种方式
        - 1. 从语音返回后的语句查询关键字，然后处理
        - 2. 使用其他的唤醒词 （不同唤醒词进入不同模块）





