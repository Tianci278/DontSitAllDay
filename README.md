# DontSitAllDay
DontSitAllDay is a stupid application using OpenPoseDemo to count squats. 它每隔一段时间，就会打开OpenPoseDemo，然后你必须要对着摄像头做一定数量的蹲起，它才会自动关掉。

# 食用方法
1）在使用DontSitAllDay前，必须要安装OpenPoseDemo（关注公众号TIANCI SAYS，回复“HPE好酷”来获取安装教程）；
2）OpenPoseDemo安装完成后，下载整个DontSitAllDay库到OpenPoseDemo的根目录中；
3）将execute_op.bat从DontSitAllDay剪切到OpenPoseDemo的根目录中；
4）运行countSquat_realTime.py，你就……可以等着做蹲起了。

# 参数调整
countSquat_realTime.py中有两个可调整参数。一个是waitTime，单位是秒，其数值代表的是程序每次强迫你做蹲起的间隔时间；一个是numOfSquats，单位是个，其数值代表你每次要做多少个蹲起程序才会关闭。
