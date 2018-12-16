项目知识点

项目主要就是分后端和前端。

后端包括 models.py、admin.py、数据库和后台。models.py 和数据库是对应的，所以创建完 model 要执行 migrate，migrate 就是迁移到数据库，一个 model 就是数据库的一张 table。后台是根据 model 创建的，是通过 admin.py 实现的。后台添加的数据会直接存到数据库里。

前端包括 urls.py、views.py 和所有 html 文件。url 和 view 是对应的，每次在 view 里面写完函数就会添加一条 url。url 是页面的入口，view 对应 url，view 前面连接 html 后面连接数据库。打开一个页面的时候，先输入 url，然后 url 找到 view 里对应的函数，view 里的函数的作用都差不多：从数据库里取值，分享到前端页面。banner_list = Banner.objects.all() 这样的语句就是从数据库取值的意思，然后把取到的内容，都一起放到了 ctx 里，通过return render 语句把内容分享到前端页面，从而实现数据库和前端的连接。在 html 里，{{}} 里放的是变量，可以理解成是取值的意思，比如 {{banner.text_info1}} 可以理解成，取 banner 里的 infor 。

(所以说就是，models 创建数据库表格，框架，admin 添加数据到数据库，views 从数据库取数据，整合分享到前端页面，url 连 views，实现页面的展示。)

不过大体上来说，方法和顺序都是一样的

创建模型，迁移到数据库，admin 注册，后台添加数据，views 导入模型，创建函数，从数据库获取数据，分享到前端页面，添加 url，修改 html

html 的修改也差不多是同一个模式，for 循环取值，替换变量

我觉得一个项目 80% 以上的内容都是用这种方法做出来的，Django 差不多就是这么建网站的

Flask 创建网站的逻辑也是这样的，Django 还容易一些，Flask 没有后台，要自己创建后台，实现后台的各种功能，同样的项目，Flask 的代码量差不多是 Django 的 3 倍。

从结构上来说，Django 项目大致分为项目、应用、数据库、模型、后台、视图、路由、样式、表单这些

我们做的这个项目，项目名称是 xxkt，应用名是 myapp，数据库用的是 mysql，创建的数据库名叫做 xxkt_db

elearning 只是一个文件夹，可以当做是个简单的容器

而 myapp 和 xxkt 则是包，就是 package

包和文件夹差不多，区别是包下面会有一个 __init__.py 文件

本质是一样的，就是放文件

不过，可以从包里导入文件，就是最开始写的 from ... import ...

创建项目命令是 Django-admin startproject

一个项目可以有多个应用，一个应用可以被多个项目重复使用

项目除了包含应用，还有配置文件

再说一点数据库的内容

数据库常用的命令有几个，SHOW databases; USE ..._db; SHOW tables; DESC ...db; 这些，最常用的是查询 SELECT * FROM ...

最上面的几张表是项目自带的

是从 settings 里的 installed app 里 migrate 到数据库的

下面的都是从 myapp 里的 models 里迁移过去的

迁移分为两步，第一步是 makemigrations

这一步的目的是生成中间表，migrations 文件夹，并没有迁移到数据库

migrate 是把中间表转化为数据库的表，所以执行 migrate 的时候会显示 applying 0001_inital.py...ok 这样的结果

模型和数据库里的 table 是对应的，一个 model 对应数据库里的一张 table，迁移完成以后，下面这些以 myapp 打头的都是从 models.py 里迁移过来的

model 的属性和 table 的属性也是一一对应的

其实 models 里的每一个属性对应数据库里的一列，数据库的一列叫做一个字段，也就是属性和字段一一对应

这个汉字，是在后台显示的标签，其实是叫 verbose_name，如果不是 foreignkey，verbose_name 可以不写

有 foreignkey 的时候要加 verbose_name

on_delete=True 的意思是关联删除，比如删掉 teacher 的时候，是不是也删掉这个老师对应的 course

foreignkey 是多对一的意思，是类和类之间的关联关系之一，一共有三种关系：一对一，多对一和多对多

多个 course 对应一个 teacher

__str__ 和 verbose_name, verbose_name_plural 

查询语句大部分都是这样：banner_list = Banner.objects.all()，是从数据库里取值的意思

有几个不一样的形式

一个是 filter

这个是按条件查询的意思

把满足条件的取出来

order_by 是排序的意思

course_list = Course.objects.order_by('pub_date').all() 查出所有的 course，按时间排序列出来

还有一个 get

get 是取一条的意思

一般是根据 id 取

GET.get 不是从数据库取的值，是从前端 html 的表单里取的，我不太懂内部原理，我觉得应该是从服务器取值的意思

还有一个 count，查询的意思，查询个数

在 index 里用了，统计老师、学生、课程的个数

还有一点

就是关联查询

前端 html 里有一个 set

取出来查询集

说一点 admin 的内容

管理后台

首先是创建账号

createsuperuser

然后就是 runserver

admin.py 就是导入模型、register 注册

自己更改后台的名字

说一点模板的内容

先说 HTML、CSS 和 JavaScript 都是干什么的，它们之间有什么关系

html 不是一门编程语言，是一种标记语言，我的感觉是其实 HTML 和 PPT 意思差不多，只是 HTML 的内容更多一些，大体相同，是用来展示页面的，并没有处理事件的功能

HyperText Markup Language，超文本标记语言

HTML 构成了我们看到的网页的支架

决定了网页的结构

包括标题、段落、列表、文本框这些

CSS 是用来控制外观的

它决定了 HTML 的属性如何显示

包括颜色字体这些

可以使网页更丰富更好看

JavaScript 是用来控制行为的，用于和用户交互

比如鼠标停在上面回有什么样的动作这些

我们的项目的首页，分类的 6 个图标把鼠标停在上面就会向上打开，还有加入会员开始学习这些按钮，鼠标停在上面会有变化，就是通过 JavaScript 实现的，可以让网页更加人性化

有一个很好的比喻

写 HTML 就像是盖房子，CSS 就像是装修，JavaScript 就像是感应门、声控灯，有一个触发，就会产生相应的变化

h1-h6 都是标题

字号依次减小

p 段落也是放文字的

p 可以嵌套 span

class 是控制样式的

是在 CSS 和 JavaScript 里用的，CSS 会根据 class 控制样式

还有一个 div

div 并不是指特定的一个元素

div 算是一个容器

存放其他元素

文档布局用的

CSS 可以通过 div 的 class 控制样式，效果一般就是一大块儿内容整体发生变化

HTML 不能完成功能

这些功能是在后台实现的

view 和 model 这些

模板

模板就是静态页面嵌套动态变量和标签

静态页面就是 HTML 的东西

变量就是{{}}里的东西

标签就是 {%%}

标签里面就是一些简单的程序语句

还有最后一点，就是模板继承

extends

block content

继承就是实现代码的重复利用省事

讲一下 url

url 就是一个地址

Uniform Resource Locator，统一资源定位器

就是一个 web address

这个 urls.py 里的 url 都是由三部分组成

路由、视图和名称

路由是在浏览器里的地址栏里用的

在浏览器输入地址以后，就可以通过第二个 views.vip 找到 views.py 里的 vip 函数

也就是第二个 view 是起到导向作用的

Django 里有两对儿是形影不离的

model 和数据库

url 和 view，是一种映射关系，一对一或多对一

一般就是一对一

最后就是 name

为什么要多加一个 name 呢？

嗯，这个 name 还是有点复杂

有两个地方用到了 name

先说第一个

第一个用在 view 函数的重定向里

上面 reverse 里的就是 name

下面没有 reverse 的里面是 url 路由

我举个例子，就用 logout 吧，还简单一些

不加 reverse 只写 HttpResponseRedirect 里面用的就是路由不是 name

用 name 更好

所以总是加 reverse

还有一处是用在 html 里

login 的两种不同写法

为什么要增加一个 name 呢？

肯定是有好处

要不然也不会有人多此一举

好处就是省事

就是说

如果更改了 url，name 没变，那么，其他的地方就不用改

如果没有 name

那么一个地方改了，其他所有用到的地方都要改过来

好了 url 基本上说完了

说 view

view 是干啥的呢？view 是处理东西实现功能的

就是汽车的各种外面看不见的系统的作用

真正起作用的东西

web 开发其实就是请求响应机制

前面页面发一个请求

然后返回一个响应

view 就是接收请求返回结果的

举个例子

就是我们的网站的首页

当输入 http://127.0.0.1:8000 的时候，其实就是一个请求

能够有一个页面显示出来就是一个响应

能够出现轮播图、博客、分类这些，都是从view 里来的

在 index 函数的 ctx 里，把 'banner_list':banner_list, 这句话注释掉

前面首页就没有轮播图了

原因就是 view 的函数返回的时候没有了 banner_list

return 是返回

就是响应

简单说，就是一个动作，会产生响应的变化，会有一个反馈过来

views.py 里一般有两种东西，一个是函数 def ，一种是类 class

功能都是一样的

处理请求

返回结果

处理呢

一般都差不多

就是取数据

分享数据

有一点要说的就是参数

有些函数里会传参数

bid，cid 这些

参数的作用就是找出特定的某一个东西

参数是在函数后面括号里的东西

其实是有三个地方用到了

一个是

blog-detail

一个是 course-detail

还有一个评论 comment

也用到了 bid

这些有个共同特点

就是要指定某一个

哪一个课程的课程详细

哪一篇博客的博客详细

给哪一篇博客写评论

因为有很多课程博客，所以一定要有个参数来指定确切的一个

举个例子

比如很多人去参加婚礼，有一辆车停在不对的地方了，人们一般会说车牌号是多少多少的车主把车挪一下，通过车牌号来指定某一辆车。而不能直接说把车挪一下，这么说会造成混乱，有很多车

这种事情在现实生活中有很多很多

通过数字编号来确定某一个

身份证号、学号、门牌号

大概就是这些

render 和 redirect，说完就剩的不多了

render 就是渲染

return render(request, 'index.html', ctx)

我的理解

ctx 就是 context 的缩写

ctx 里面有很多从数据库里取出来的数据

banner_list、category_list 这些

渲染的意思

我感觉就是

把数据放到 index 页面里

分享到前台

前面输入一个 url

然后 view 里的函数处理

返回一个渲染后的页面

展示出来

request 和 response

说一下重定向 HttpResponseRedirect

重定向就是跳转到别的地方

如果一个函数

最后是 render 结尾

那就是说所有的东西都是在自己这个函数里处理的

从头至尾没有中断

而重定向就不是了

重定向是说，处理到这一句不在往下执行，而是跳到别的函数里了

要试一下才能理解

还是用 logout 吧

把 HttpResponseRedirect 注释掉，换成 render 试一下

然后点击注销看一下差别

什么数据都没了

分类

课程

博客

明星学员

都没了

原因很简单

原因就是用了 render，没有用 HttpResponseRedirect

用了 render 所以从头至尾都没有中断，一直在 logout 这个函数里，因为这个函数里没有处理过程，就是说没有去数据库取值，没有 ctx 这些，所以渲染的时候，没有数据可以传到前面去，所以什么都不显示

而 HttpResponseRedirect

就不一样了

执行到这一句以后

就跑到 index 函数里了

然后是取值分享渲染这些

所以会有一个完整的页面

搞编程的这些人很聪明

想方设法省事

各种重复利用

很聪明

view 类

我们这个 views.py 里大部分用的是函数

有三个用的是类 class

最开始是用的 def login

这个其实就引到了要讲的表单了

不一样的地方是

这些类的数据不是从数据库取的

是从前面网页里取的

类和函数的功能差不多

不过从前面表单里取数据比较麻烦

而 Django 自带的类里面就已经写好了，已经实现了从表单中取值再处理的功能了

所以继承是最省事的

如果写成函数就会比较复杂，因为还要去写一个 forms.py 然后要定义属性，然后要分享到前台，再取数据，再处理很麻烦

简单说一下表单的数据传输的流程

其实还是一个简单的比喻，更好理解

其实整个处理过程就像是加工一个零件

通过 url 找到工厂的地址

views 就是个工厂

数据库呢就像是库房

前台呢，其实就是外人在大门口看到的，并不了解内部加工原理

这个过程可以这样说

通过 url 找到工厂

参数其实就是要求

比如加工一批零件，要有图纸，大小尺寸形状这些要求

参数是从外面传进来的

是客户的要求

客户找到工厂以后

提出要求

其实就是一个请求

request

工厂拿出一个产品

返回一个结果

就是一个 response

中间的过程呢

有从数据库里取原材料

有一些加工

比如 order_by

filter

等等

加工以后

有一个喷漆包装的渲染过程

都做好之后，交货

返回

大概就是这样

有两个点没说到

一个是 {% url 'register.html' %}

为什么这么写不行

因为里面要用 name

而 urls.py 里的 url 的 name 没有叫做 register.html 的

所以匹配不上

这种 href 里带有 .html 的写法

一般是用于静态页面跳转的

找到这个文件的意思

是一种简单的联系

并没有用到内部的功能

就是说绕过了 Django

一般 base.html 里

那些 CSS、JavaScript 文件都是这么找到的

而 {% url ‘register’ %}

这么写其实就通过这个 name = register

找到这条 url

从而找到 views.register

从而跳到 views ，用到了 register 函数，实现功能

第二点要说的是

带参数的路由

要传参数的

这个和 views 里的函数的参数是对应的

通过 id 指定哪一篇

所以详细都要有一个 id

说一下表单

表单是接受输入的

如果只是显示信息就不用表单

如果要输入东西

就要用到表单

从 <form> 开始，到 </form>结束

一个登录、一个注册、一个评论

其实去 base.html 里搜的话

还有两个

一个是提交邮箱、一个是搜索框

不过我们没有做这两个功能

表单就是接收前面输入的数据的

其中

input 就是个输入框

button 点击跳转用的

一般嵌套一个 a 链接

placeholder

是显示用的

然后 input 的属性里

除了 type

placeholder 这些

还有 name

name 的作用

这个 name 是 input 的 name

可以通过 name 拿到输入框里的数据

通过 request.POST.get('username') 就拿到了前面输入的用户名



是有一个判断

在 login 里 

如果前面输入的用户名密码

和数据库里用户名密码相同



就登录

在 form 表单里

有两个东西要写明

一个是提交的数据的目的地，一个是提交方式

目的地是个 url

是 action 

我说一下数据传输的过程

用 register 举例吧

看一下，数据是怎么从前端页面存到数据库里的

首先是到 register 页面

用户填写数据

然后点击注册

带有数据的表单就会发送到 action 对应的地址

然后根据这个 url 的 name 到 urls.py 找到这条 url

后找到这个 RegisterView

然后就跳转到了 views.py 

因为表单里的 method 是 post

所以这里到了 post 函数里

username = request.POST.get('username')

这句话

就取到了用户输入的用户名

密码邮箱也都是这样

下面就是实例化了一个 user

然后把从前面取到的用户名密码赋值

给了这个 user

user.save()

就把这个带有数据的 user

保存到数据库里了

类的实例化，就是 user = XXUser()

这样数据库里就增加了一个用户

然后登录的时候

就是前面输入的数据和数据库里的数据做对比

相同就登录

不同就报错

GET 和 POST

其实就是两种不同的请求方式

POST 一般就是提交的意思

提交数据

GET 一般是获取的意思

提交用户名密码

提交评论

用 POST

get

看地址栏，这里会把输入的信息显示出来

POST.get

意思是

从通过 POST 方法提交的数据里获取

还有一点

应该是最后一点了

很简单

就是绑定表单和未绑定表单

未绑定表单就是空表单

是最开始跳转到登录注册页面的时候展示出来的表单

是空的

绑定表单就是填好数据的表单

是提交以后的那个带数据的表单

是 request.POST.get

就是从这个表单里取数据的

我们看不到

因为已经提交了

但是有这么个东西

未绑定表单就是考试的时候刚发到你手里的空白试卷，绑定表单就是你已经答完的试卷，里面都有内容了。但是这个已经答完的试卷是要交的，交了以后你就看不到了，但是还是有的，会根据这个绑定表单给你批改，打分，虽然你看不到，但是是有这个东西的

老师发试卷是一个 get

交试卷是个 post
