# zero-imagine

20到21世纪计算机由“0”和“1”构造原始数字存储空间，对于计算机技术的发展精神而言，或许不外乎我们这一代人将“0”写下现在，将“1”留给未来。

该项目目的是创建一个功能强大的操作助手，使得她拥有灵活变化的功能以及能够适应众多的应用场景。

# 介绍

计算机在最开始仅用于计算，后来人们将电路集成到屏幕上，并能够显示简单的字符。随着计算机技术的不断发展，后来渐渐发展出了丰富多彩的图形化操作系统。现在我们希望能创建具有强大功能组织能力和能够适应多种环境的助手来解放业余生活和提高工作效率，根据如今的社会生产科技水平，助手不仅需要具有强大的运算逻辑能力，还需要具有便捷的操作逻辑能力。


# Zero-imagine功能设计书（拟订）


综述：该项目目的是创建跨平台的智能助手，旨在将计算机功能操作便捷化，使得人们能够更加方便地使用和管理计算机等智能电子设备。项目设计流程确定如下，确定功能－集成代码块－构建核心驱动器－整理辅助功能－优化工作，前三步流程同步进行，但是整个项目具体方案依然按照项目设计流程顺序编写。

# 1.确定功能

助手需要便捷的操作逻辑能力和强大的运算逻辑能力。

## 操作功能：

## 1)默认操作模板（光标）：

a)左键：单击时选择（按下和松开）；再单击任意取消。长按左拉滑动（查看右侧内容）。长按右拉滑动（查看左侧内容）。长按上拉滑动（查看下方内容）。长按下拉滑动（查看上方内容）。双击打开。

b)中键：单击时抓取/放下（按下）。长按抓取移动，松开放下。滚动时滚动页面（允许滚动时）。

c)右键：单击时打开助手/临时助手（按下和松开）；再单击界面外隐藏（按下和松开）；如果在助手成端的功能块上，使用单击/双击左键（按下和松开），则选择使用该功能，长按左键（不松开）取消选择使用。长按上拉、左拉、右拉自定义（可以打开助手脚本，如变透明、变形、打开多个外挂助手等）。长按下拉隐藏；隐藏前上拉取消隐藏。

## 2)拓展操作模板（其他输入）：

a)文本标准化：将所有操作数据规范到utf-8，无论功能块底层数据如何，面向客户的操作脚本（操作指令集）使用utf-8标准。

b)人-机快速操作指令集：可以通过助手自定义快捷键来定义、切换不同指令集。

c)助手感知模式：助手使用多种交互模式，比如快速模式、编辑模式和自动模式等。不同模式可以对应不同操作指令集，可以由客户自行定义。

## 3)外挂协议（难点）：

a)绝对置顶：接管所有操作设备输入输出。

b)底层监控：监控设备运行状态。可以接管设备输入输出。


## 运算功能：

## 1)操作功能中的文本标准化：图形化快速编码器和解码器等。

## 2)数据库：

a)总数据库：包含所有文件。同时额外增加标签作为分类（同文件名称管理）。

b)功能模块数据库：根据标签归类。进一步划分表示不同的功能，实际上可以是别名库。

c)图形管理数据库：根据标签归类。也可以是别名库，管理所有图形化脚本（utf-8）。

## 3)助手主面板：

a)模式识别（要求较高）。侦测不同操作场景。

b)异步功能（必须）。可以发出异步线程，侦测操作。

c)界面属性可快捷操作（比如快捷缩放界面大小、调整透明度、调整旋转和进行动作等）。

d)可成端功能块。

e)可调用临时助手。

## 4)临时助手：

a)所有临时助手同级。

b)临时助手可根据场景自定义（临时助手面板具有自定义按钮，可以转入编辑器，对自身进行特例化自定义，保存后在特定场景取代默认临时助手）。

c)临时助手具有默认模板，如有需要，在界面数据库进行修改。

## 5)编辑器（外挂）（要求较高）：

a)遵守操作规范（可自定义），可使用临时助手。

b)可制作图形化文本块，位置、形状可调。

c)可自行建立文本块模板。

d)可自行设置快捷键进行模板操作。

e)可自定义功能板（特例化临时助手），包括内容更改，新增固定功能板。

## 6)提示器（外挂）（要求较高）：

a)遵守操作规范（可自定义），可使用临时助手。

b)学习和分析操作数据。

c)可根据提示互动进行操作。

d)可调用功能模块（包括编辑器）。

## 7)外挂器：将功能模块外挂。

## 8)外挂协议（要求较高）：

a)遵守助手模式识别要求。

b)遵守外挂操作规范（可自定义）。

c)需要向功能数据库加入事件管理器，由事件触发功能。

d)除了总数据库和自定义数据库，数据库需要分离自定义栏和系统原始栏。

e)网络敏感操作警告。

f)冲突警告。

# 2.集成代码块

由于助手设计涉及许多快捷使用数据库的功能（即时自定义），代码就需要非常高的逻辑独立性，并且需要块的功能尽可能单一。此外，在代码块的可视化上，同样要求准确分类和来源独立。
详情见《Zero-imagine集成代码规范协议书（拟订）》。

# 3.构建核心驱动器

核心驱动器在传统意义上可以看作进程和线程管理器，也可以看做是代码编译器或者是浏览器内核之类的文本驱动器。它包括：图形化框架，内置编译器和接口选择器。

## 1）图形化框架：

a)助手主体：

b)临时助手：

c)窗口面板（外挂）：

d)局内面板（特例化临时助手）：


