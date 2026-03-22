# Enqiao Lu - Personal Website

## 简介

这是一个为Joe（陆恩乔）设计的精美个人网站，展示了他的学术背景、研究成果、荣誉奖项和技能特长。

## 网站特色

✨ **现代设计**
- 渐变背景和流畅动画
- 卡片式布局，清晰易读
- 专业的配色方案（蓝紫色渐变）

📱 **完全响应式**
- 适配桌面、平板、手机
- 移动端友好的导航菜单
- 流畅的滚动体验

🎨 **交互效果**
- 平滑滚动导航
- 卡片悬停动画
- 打字机效果
- 滚动淡入动画
- 返回顶部按钮

📄 **完整内容**
- 个人简介
- 教育经历（港中深本科）
- 研究经历（A*STAR, CUHK-SZ）
- 论文发表（Transportation Research, 国家发明专利）
- 荣誉奖项（Dean's List, 奖学金等）
- 技能特长（深度学习、编程、语言）

## 文件结构

```
personal-website/
├── index.html          # 主页面
├── styles.css          # 样式表
├── script.js           # 交互脚本
└── README.md           # 说明文档
```

## 如何使用

### 本地预览

1. 直接用浏览器打开 `index.html` 文件
2. 或者使用本地服务器（推荐）

使用 Python 启动本地服务器：
```bash
cd C:\Users\15957\WorkBuddy\Claw\personal-website
python -m http.server 8000
```
然后访问：http://localhost:8000

使用 VS Code 的 Live Server 扩展也可以。

### 部署到公网

要让所有人都能访问，可以部署到以下免费平台：

#### 1. GitHub Pages（推荐）
1. 在 GitHub 创建一个新仓库（例如：`enqiao-lu.github.io`）
2. 将 `index.html`、`styles.css`、`script.js` 上传到仓库
3. 进入仓库 Settings → Pages
4. 在 Source 部分选择 `main` 分支，点击 Save
5. 几分钟后，访问 `https://enqiao-lu.github.io`

#### 2. Netlify
1. 登录 https://www.netlify.com
2. 将整个文件夹拖到 Netlify 的部署区域
3. 会自动生成一个可访问的网址

#### 3. Vercel
1. 登录 https://vercel.com
2. 导入项目文件夹
3. 自动部署，获得免费域名

#### 4. Cloudflare Pages
1. 登录 Cloudflare Dashboard
2. 选择 Pages → 创建项目
3. 上传文件或连接 Git 仓库
4. 自动部署

## 自定义内容

### 更换头像

在 `index.html` 中找到：
```html
<div class="avatar-placeholder">
    <i class="fas fa-user"></i>
</div>
```

替换为：
```html
<img src="your-photo.jpg" alt="Enqiao Lu" class="avatar-photo">
```

并在 `styles.css` 中添加：
```css
.avatar-photo {
    width: 350px;
    height: 350px;
    border-radius: 50%;
    object-fit: cover;
    border: 4px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}
```

### 修改配色方案

在 `styles.css` 的 `:root` 部分修改颜色变量：
```css
:root {
    --primary-color: #2563eb;      /* 主色调 */
    --primary-dark: #1e40af;       /* 深色主色调 */
    --primary-light: #60a5fa;      /* 浅色主色调 */
    --secondary-color: #10b981;    /* 次要颜色 */
    /* ... 更多颜色 */
}
```

### 添加社交媒体链接

在 HTML 的 Hero 或 Footer 部分添加：
```html
<a href="https://github.com/JoeLu20051115" class="social-link" target="_blank">
    <i class="fab fa-github"></i>
</a>
```

## 技术栈

- **HTML5** - 语义化标签
- **CSS3** - 现代特性（Grid, Flexbox, 变量, 动画）
- **JavaScript** - 原生 ES6+，无需依赖
- **Font Awesome** - 图标库
- **Google Fonts** - Inter 和 Playfair Display 字体

## 浏览器兼容性

- Chrome/Edge (最新版)
- Firefox (最新版)
- Safari (最新版)
- 移动端浏览器（iOS Safari, Chrome Mobile）

## 性能优化

- 无外部 JavaScript 依赖
- 使用 CSS 变量便于维护
- 响应式图片（可添加）
- 优化的动画性能（使用 transform 和 opacity）

## 未来改进建议

1. 添加个人照片
2. 集成 Google Analytics
3. 添加深色模式切换
4. 添加博客/笔记页面
5. 添加项目展示案例
6. 添加多语言支持（中英文）
7. 添加 PDF 版本 CV 下载链接
8. 优化 SEO 元标签

## 联系方式

- Email: 124090411@link.cuhk.edu.cn
- Phone: (+86) 159-5715-1440

## License

MIT License - 可自由使用和修改

---

**"Do the hard but right thing."** - Enqiao Lu
