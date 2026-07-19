# 论文插图审美证据库

本文件记录参考论文中的用户偏好、源文件证据和候选作图规则。最终 Skill 只吸收经过多篇论文支持或被用户明确指定为默认偏好的规则。

## 记录约定

- **用户偏好**：用户明确指出的美观点，不改写成客观定律。
- **技术证据**：从 LaTeX、PDF 矢量对象或渲染图中确认的实际实现。
- **候选规则**：可以指导 Agent 作图的暂定规则；后续论文可以加强、限制或推翻它。
- **证据强度**：`1/N` 表示目前仅有 N 篇论文中的 1 篇支持，不代表规则已经定型。

## 全局配色系统：跨图型共享，按组合调用

### 用户对 Skill 结构的修正

目前积累的颜色不应被割裂成“统计图专用色”和“pipeline 专用色”。统计图、pipeline、module diagram、comparison layout、表格以及以后学习的 demonstration figure，都应优先从同一个全局配色库中选色。图型只影响颜色承担的角色，不限制一套颜色可以出现在哪类图中。

颜色必须以**经过验证的组合**为单位调用，而不是从不同论文中各挑一个喜欢的 Hex 随意拼接。除共享中性色外，一张图默认先选择一个主组合，再从中取满足当前语义所需的最小子集。

### P1 — 柔和科研五色三级色板

适合多个类别、模型家族、阶段或 scale 层级。五个色相已经在同一张图中共同出现并保持协调；每个色相内部的浅、中、深是固定 RGB 色阶。

| 色相家族 | 浅色 | 中色 | 深色 |
|---|---:|---:|---:|
| 橙 | `#F9CB8A` | `#F7BA64` | `#F5A83D` |
| 珊瑚红 | `#FBA09D` | `#F86762` | `#F5433D` |
| 草绿 | `#B3CDA2` | `#9EBF88` | `#88B06D` |
| 紫 | `#D0B3FF` | `#A984E6` | `#7A5DE1` |
| 矢车菊蓝 | `#AEC6FE` | `#86AAFE` | `#5D8DFD` |

- **组合方式**：跨类别使用不同色相；同一类别的 size、scale 或阶段使用该色相的浅→中→深。
- **默认强调**：重要方法使用对应家族的深色；baseline 优先使用 `#BFBFC5` 或 `#D4D4D8`。
- **透明度分工**：普通线、点和色阶优先使用固定 RGB 与 `alpha=1`；气泡等面积重叠对象可从 `alpha≈0.75` 起步。
- **证据**：橙、红、绿、蓝四组在 Paper 01 与 Paper 02 中逐个 Hex 复现；完整五色组已通过 Forward Test 01。

### P2 — 珊瑚红与矢车菊蓝的二元对比组

适合两个方法、两条路径、旧/新表示或其他暖冷二元对比，也可以用于 pipeline 中的两条语义流。

| 角色 | Hex |
|---|---:|
| 暖珊瑚红 | `#FB8E89` |
| 冷矢车菊蓝 | `#6F9AFE` |
| 统一结构深灰 | `#595959` |

- **组合方式**：红蓝承担对等的两个主体，深灰统一用于边框、连接或结构骨架。
- **防误用**：`#FB8E89` 与 P1 的浅红 `#FBA09D` 很接近，但不是同一色阶。不要在同一图中把两者当成两个不同类别，也不要混用后声称它们属于同一浅→深家族。
- **证据**：Paper 01 Figure 2 同图验证。

### P3 — 红、绿、蓝的状态区域与注释组

适合阈值图、regime map、风险/成功区域、理论与观测对照，也可迁移到需要“主关系 + 背景状态区”的流程或概念图。

| 角色 | Hex | 推荐处理 |
|---|---:|---|
| 主关系红 | `#F5433D` | 实色线/边界；同色背景可用 `alpha≈0.15` |
| 观测绿 | `#88B06D` | 实色点/marker |
| 状态蓝 | `#5D8DFD` | 同色背景可用 `alpha≈0.15` |
| 暖色注释填充 | `#EF9463` | `alpha≈0.60`，配 `#C46032` 描边 |
| 冷色注释填充 | `#002FAB` | `alpha≈0.30`，配 `#496EC8` 描边 |
| Grid | `#D3D3D3` | 实色、置于数据下层 |

- **组合方式**：红、绿和蓝直接复用 P1 的深色锚点，因此可以安全共同出现；两组注释色只用于局部 callout，不扩张成新的大面积类别色。
- **证据**：Paper 01 Figure 3 同图验证，并通过 Forward Test 01。

### P4 — 深红、深蓝与紫色的语义流组合

适合多个语义维度、数据流、阶段、scope 或 callout。虽然来源是 pipeline figure，但这套深色组合也可用于统计图的三类重点曲线、表格分组、时间线或其他图型。

| 语义角色 | Hex |
|---|---:|
| 深红主色 | `#B1001C` |
| 深蓝主色 | `#003776` |
| 深紫文字/强调 | `#310067` |
| 淡紫边框/callout | `#907CBB` |

- **组合方式**：深红与深蓝承担两个主要维度，深紫/淡紫作为第三类重点机制或解释性 callout；主色同步用于相关标题、边框和箭头。
- **同组合的渐变扩展**：Paper 04 Figure 3 进一步验证了以下卡片渐变端点，可在任何适合的图型中与 P4 共同使用：蓝色实体 `#92BFFF ↔ #0C2734`、深浅灰实体 `#939595 ↔ #DADADA`、白灰实体 `#FFFFFF ↔ #DADADA`、红色 trainable 实体 `#901113 ↔ #DFBCB7`。渐变方向应服从版面和阅读方向，不写死为固定角度。
- **中性骨架**：搭配 `#000000`、`#666666`、`#A5A5A5`、`#D9D9D9` 和 `#FFFFFF`。
- **防误用**：这组颜色整体比 P1 更深、更正式。若选择 P4，不要再随意加入 P1 的粉彩橙绿，使整图同时出现两种不一致的饱和度和视觉气质。
- **证据**：Paper 03 Figure 3 同图验证。

### P5 — 灰色与焦橙的 workflow 对比组

适合 baseline/proposed、previous/ours、人工/自动等非对称对比，也可用于统计图 panel 背景、表格分区、流程图、标题条或 demonstration 分组。

| 角色 | Hex |
|---|---:|
| 灰色锚点 | `#666666` |
| 焦橙锚点 | `#B34400` |
| 灰色浅背景端点 | `#A5A5A5` |
| 橙色浅背景端点 | `#F3BAB1` |
| 背景起点/卡片 | `#FFFFFF` |
| 主结构 | `#000000` |

- **组合方式**：大面积背景使用白→浅灰或白→浅鲑橙的低对比渐变，或者直接使用相应浅色纯色；group caption 和关键 sub-module 使用深灰/焦橙锚点。
- **防误用**：浅鲑橙背景 `#F3BAB1` 不承担高辨识度数据系列；焦橙 `#B34400` 才是文字、描边或重点对象的锚点色。渐变是可选方案，不是这套配色成立的前提。
- **证据**：Paper 04 Figure 2 同图验证。

### 共享中性色骨架

以下颜色可跨 P1–P5 使用，但仍应按角色选择，避免把多个近似灰色无意义地堆在同一图中。

| 角色 | 优先颜色 |
|---|---:|
| 主文字、主数据流、坐标框 | `#000000` |
| 强结构描边 | `#595959` |
| 次级文字、group label | `#666666` |
| 中性边框、辅助箭头、浅渐变端点 | `#A5A5A5` |
| baseline 数据对象 | `#BFBFC5`、`#D4D4D8` |
| 统计 Grid | `#D3D3D3` |
| 弱分隔线 | `#D9D9D9` |
| 表格默认/选中配置底色 | `#E6E6E6` |
| 卡片、暗图边框、暗底反白文字 | `#FFFFFF` |

### 配色选择流程

1. **先识别关系，不先识别图型**：判断需要表达的是多类别、二元对比、状态区域、多条语义流，还是 previous/ours 分组。
2. **选择一个主组合**：多类别优先 P1，二元暖冷对比优先 P2，状态/阈值优先 P3，多语义流优先 P4，非对称 workflow 对比优先 P5。
3. **只取最小子集**：简单图通常使用 1–3 个强色；只有类别数量确实需要时才启用 P1 的全部五个色相。
4. **绑定语义角色**：同一对象在曲线、module、caption、箭头和 legend 中保持同色；同一色相的浅中深表达从属层级，不表达互不相关的类别。
5. **区分 RGB 色阶与 alpha**：固定浅中深用于稳定的类别层级；alpha 用于背景区域、置信带、重叠、阴影和定位辅助线。
6. **完成可读性核验**：检查白底/暗底对比、缩放后的辨识度、灰度打印、色觉缺陷风险，以及文字和 Grid 是否仍清楚。

### 禁止的配色方式

- 不从 P1–P5 中各抽一个“看起来好看”的颜色拼成未经验证的新组合。
- 不在同图中混用同一色相的近似色并让它们承担不同类别，例如同时用 `#FB8E89` 和 `#FBA09D`。
- 不让每个 module、每条箭头和每段文字都使用强色；中性色必须承担大部分结构。
- 不仅靠颜色区分类别；统计图同时使用 marker/线型/直接标签，pipeline 同时使用位置/容器/线型。
- 不因为颜色最初来自某类 Figure 就限制其用途；是否使用由语义关系、背景和信息密度决定。

### 新颜色的准入条件

优先使用以上组合。只有现有组合无法满足类别数量、背景对比、色觉可访问性、论文品牌色或用户明确要求时才新增颜色。新增颜色应先与当前主组合比较明度、饱和度和冷暖关系，形成完整的小组合并经过实际渲染验证，而不是作为孤立 Hex 加入。

## Graphics Color Intake 01 — Learning Sewing Patterns via Latent Flow Matching of Implicit Fields

### 合并与去重

- 本轮不是另建一套“SIGGRAPH 专用色”，而是在同一个全局 Color Bank 中继续追加来源证据。颜色仍然可以跨统计图、pipeline、architecture、teaser 和结果展示使用。
- 已把前面 P1–P5 的 43 个唯一颜色正式迁入 `graphics-color-library.yaml`；P1/P3 共用的红、绿、蓝，以及 P4/P5 共用的黑、白和灰，只存一条颜色记录，由多个组合共同引用。
- 本篇新增 19 个唯一颜色。它们与旧库没有完全相同的 Hex，因此没有误删；相近但用途与组合不同的颜色（如 `#B2DEA1` 与旧草绿、`#999999` 与旧灰色）继续分开保存。

### Figure 2 / Figure 3(a–b)：SDF/UDF 蓝→橙红发散色带

PDF 中的场图是 JPEG 栅格对象，无法直接恢复生成代码。对 Figure 2 与 Figure 3 的场图像素进行比对后，其颜色轨迹与经典 `RdBu_r` 发散色带稳定匹配；Color Bank 因而保存可复现的标准色阶，而不是保存 JPEG 压缩后的随机像素偏差：

`#053061` → `#2166AC` → `#4393C3` → `#92C5DE` → `#D1E5F0` → `#F7F7F7` → `#FDDBC7` → `#F4A582` → `#D6604D` → `#B2182B` → `#67001F`

- **偏好等级**：主优先、用户明确认可。
- **正确用途**：signed distance、正负残差、带零点的连续标量场、需要冷暖两端和中性中心的 heatmap。
- **组合约束**：按完整连续顺序使用；`#F7F7F7` 对应零点/边界中性中心。除非语义符号明确反转，否则不要随意颠倒蓝端和红端。
- **禁止误用**：这不是 11 个离散类别色；不要把相邻浅色当成互不相关的模型类别。

### Supplementary Figure 4：肉色、灰色、绿色三色组合

使用 PDF 内嵌 soft mask 仅采样图案前景，并在多行、多 case 的重复区域上取稳健中位数/众数，得到：

| 角色 | Hex | RGB |
|---|---:|---:|
| 肉色 | `#EDD1C6` | `237, 209, 198` |
| 灰色 | `#999999` | `153, 153, 153` |
| 绿色 | `#B2DEA1` | `178, 222, 161` |

- **偏好等级**：主优先、用户明确认可。
- **组合方式**：三色在白底上作为等权 case / method / state 使用；文字、分隔和边框继续使用中性色，不再叠加第四个强色。

### Supplementary Figure 5：蓝、红、绿 case 家族

这些颜色来自 JPEG 压缩后的平坦图案区域，以下 Hex 取重复区域的主众数，置信度低于 Figure 4 的三色组：

- **蓝色家族**：强调 `#6F99E1` + 柔和 `#C5D5EE`。
- **红色家族**：强调 `#E38897` + 柔和 `#EDC3C7`。
- **绿色单色锚点**：`#BFCEA5`；当前没有从论文中推断不存在的浅/深配套色。
- **偏好等级**：次优先候选。用户评价为“还行、一般般”，因此已采集但不会覆盖前面明确认可的优先组合，也不会自动作为默认首选。

### 本轮结构化结果

- Color Bank：`graphics-color-library.yaml`
- 唯一颜色总数：62（旧 43 + 新 19）
- 配色组合总数：10（旧 P1–P5 + 本轮 P6–P10）
- 所有颜色同时保存 sRGB Hex、RGB、OKLCH、alpha、来源、提取置信度、组合成员关系和偏好状态。

## Graphics Color Intake 02 — The Antipodal Method

### 正文 Figure 3：薄荷绿与珊瑚橙区域组合

Figure 3 实际由 `figures/alexander-numbering_1.pdf` 和 `figures/alexander-numbering_2.pdf` 组成。颜色位于 PDF 内嵌的无损栅格球面渲染中，因此保存的是稳定的显示色锚点，而不是臆测的“未受光材质色”：

| 角色 | Hex | 说明 |
|---|---:|---|
| 薄荷绿主色 | `#A6E2B4` | 冷色区域主锚点 |
| 珊瑚橙主色 | `#F9856A` | 暖色重点区域 |
| 浅桃橙陪衬 | `#FACBBB` | 更大或更弱的暖色背景区域 |

- **核心搭配**：`#A6E2B4 + #F9856A`；浅桃橙只作为同一暖色语义的弱层级，不应被误当作第三个对等类别。
- **适用场景**：几何区域、正负有向面积、两种状态、统计图中的暖冷重点对比。
- **面积建议**：高饱和珊瑚橙的面积小于薄荷绿或浅桃背景，避免整图过热。

### 正文 Figure 5：同一暖冷逻辑的低饱和扩展

Figure 5 的颜色受到球面光照和阴影影响。提取时保留了“语义表面色 + 阴影色 + 中性球面灰阶”的结构，而不是把每一个受光像素都加入 Color Bank：

| 角色 | Hex |
|---|---:|
| 柔和橙 | `#DFB5A7` |
| 深橙阴影/次级暖色 | `#D2AB9D` |
| 柔和绿 | `#90C39C` |
| 球面浅灰 | `#F5F7F9` |
| 球面中灰 | `#E6E6E8` |
| 球面深灰 | `#CDCECF` |

- **组合逻辑**：灰色占据最大背景面积；橙和绿只承担解释性表面；深橙用于阴影、嵌套区域或同一暖色对象的第二层级。
- **与 Figure 3 的关系**：Figure 3 更明亮、更饱和；Figure 5 更低饱和、更适合带光照和空间深度的 3D/geometry diagram。两者共享暖橙 + 绿的语义结构，但不应把受光后的 Hex 强行宣称为同一个 RGB。

### Supplementary Figure 3：两套连续渐变

补充材料 Figure 3 对应 `figures/aq_accuracy.pdf`。PDF 直接包含两条 `257 × 10` 的无损色条，因此以下颜色是等间距的精确色条采样，不是从热图中估计：

#### P13：紫红→珊瑚橙误差色带

`#251255` → `#4F127B` → `#752181` → `#9C2E7F` → `#C53C74` → `#E95462` → `#FA7D5E` → `#FEAA74` → `#FED89A`

- 视觉路径是深紫、红紫、莓红、珊瑚、橙和浅金，并不是蓝色渐变。
- 适合 error、energy、density 或 log-scale heatmap；必须作为连续色带使用，不能拆成九个随意类别色。

#### P14：白→橙红单向强度色带

`#FFFFFF` → `#FEF7F6` → `#FEEFEE` → `#FDE8E5` → `#FDE0DC` → `#FCC8B7` → `#FCAD90` → `#F67F64` → `#DE2D26`

- 适合 evaluation count、计算开销、稀疏→密集或最小值→最大值的单向 heatmap。
- 白色端点在白色论文背景上可能消失；需要保留坐标框、cell 边框或明确的非数据背景才能看清零值区域。

### 本轮合并结果

- 新增 26 个唯一颜色；白色端点 `#FFFFFF` 直接复用旧库的 `paper-white`，没有重复创建。
- Color Bank 现有 88 个唯一颜色和 14 套组合。
- `#F9856A` 与补充材料色带中的 `#FA7D5E` 肉眼接近但并不相同；因为它们分别承担离散区域锚点和连续渐变 stop，继续分开保存。

## Graphics Color Intake 03 — Matérn Noise for Triangulation-Agnostic Flow Matching on Meshes

用户只认可并要求保留 Figure 4 最右侧三只 Stanford bunny 中的绿色、橙色和蓝色；本篇其他颜色不进入 Color Bank。对应原图为 `figs/noise_sample_schemes.jpg`。在右半区兔子前景中排除白底、黑色标注、极暗阴影和镜面高光后，对三个色相区域分别聚类，保留以下代表显示色：

| 角色 | Hex | 说明 |
|---|---:|---|
| 浅鼠尾草绿 | `#CACCA2` | 三色中最浅、最低饱和的柔和成员 |
| 柔和橙 | `#D58B53` | 暖色强调 |
| 钢蓝 | `#7196AC` | 冷色结构锚点 |

- **组合规则**：三色作为固定组合 P15 保存；绿色和蓝色可承担较大面积，橙色用于较小的注意力区域。
- **提取限制**：原图为 JPEG 且表面带光照，Hex 表示稳定的显示色聚类中心，不冒充未受光材质参数，置信度记为 `medium`。
- **合并结果**：三个颜色均与旧库无完全相同 Hex，因此新增 3 个唯一颜色；Color Bank 现有 91 个唯一颜色和 15 套组合。

## 目标 Skill 的确定范围：学术统计图

### 触发范围

只要 Agent 需要创建、修改、重绘或审查用于论文、报告或实验分析的**统计结果图**，就应触发本 Skill，尤其包括使用 Python、Matplotlib、Seaborn 或 Plotly 绘制：

- 折线图、收敛曲线、scaling curve；
- 柱状图、分组柱状图、堆叠图；
- 散点图、气泡图、相关性图；
- 误差棒、置信带、分布图、箱线图；
- 热力图以及由多个统计坐标轴组成的 multi-panel figure。

即使用户只说“用 Python 画一下这些实验结果”，没有主动提到审美，本 Skill 也应自动生效。

### 非触发范围

- 生成样例、重建结果、照片或渲染结果的 demonstration grid；
- 模型架构图、流程图、概念示意图；
- 纯装饰插画、封面图和非数据驱动的视觉设计。

这些图型以后可以有独立的审美分支，不应机械套用统计坐标轴、Grid 或 zoomed inset 规范。

### 建议写入最终 Skill frontmatter 的触发语义

> Create, restyle, or review publication-quality statistical result figures, especially Python/Matplotlib charts such as line, bar, scatter, bubble, distribution, uncertainty, scaling, correlation, and multi-panel plots. Apply the learned academic standards for typography, complete frames, restrained grids, calibrated color palettes, transparency, zoomed insets, annotations, layout, and vector export. Do not use for qualitative demonstration grids or architecture diagrams.

### 每次画统计图都必须检查

1. **字体**：全图保持同一字体家族和清楚的字号层级。默认使用干净、可嵌入的 sans-serif（Helvetica、Arial 或 DejaVu Sans）；若论文正文或目标 venue 明确使用 serif，则统一跟随正文。不要混用多种字体，也不要依赖未安装字体静默回退。
2. **完整边框**：统计坐标轴强默认保留四条 spine，基准线宽约 `0.8 pt`。只有在极小 sparkline 或完整框明显制造噪声时才例外。
3. **颜色**：避免 Matplotlib 默认循环色和纯 RGB 原色。先按语义关系从全局 P1–P5 中选择一个主组合，而不是把统计图限定为 P1；baseline 用中性灰，重点方法用更深、更清晰的锚点色。颜色之外还应使用 marker、线型或直接标签增强可辨识性。
4. **Grid**：需要辅助数值比较时，使用约 `#D3D3D3`、`0.5 pt` 的浅灰 Grid，并置于数据下层。若 Grid 对阅读没有帮助，可以关闭，但必须是有意识的选择。
5. **刻度与尺度**：根据数据语义选择 linear 或 log，不盲从自动刻度。跨度大且强调倍率关系时使用 log 轴与人工主刻度；刻度数量以能估计数值但不拥挤为准。
6. **透明度**：用固定浅/中/深 RGB 色阶表示同一系列的尺寸层级；用 alpha 表示背景区域、置信带、重叠或定位辅助线。背景区域通常从 `alpha=0.10–0.18` 起步，重叠气泡可从 `0.75` 起步，ROI 连接线可从 `0.5` 起步。
7. **局部放大**：当关键曲线挤在一起时，使用 zoomed inset（用户口语中的 “Zoom out”，技术上是局部 zoom-in）。必须同时包含主图 ROI、1–2 条低透明度连接线、独立且更稀疏的刻度，以及对 legend 和关键数据的遮挡检查；不要把 inset 当装饰。
8. **标注与布局**：少量短摘要优先放进图内稳定空区，并在多个 panel 中保持统一锚点。多面板图按信息量分配列宽、压缩重复 tick labels 和空隙，不默认等宽等高。
9. **强调层级**：粗体只用于关键结论、panel summary 或 proposed method，不要把所有标签和刻度全部加粗。
10. **交付检查**：优先导出 PDF/SVG 矢量版本，同时提供高分辨率 PNG；重新渲染检查文字裁切、重叠、字体替换、legend/inset 遮挡和灰度可辨识性。

### 强制项与条件项

- **强制检查**：字体一致性、边框选择、色板、Grid 决策、刻度、图层顺序、标注避让、导出与视觉核验。
- **条件启用**：log 轴、背景透明区域、置信带、气泡透明度、zoomed inset、非对称 multi-panel layout。
- “遵循审美标准”意味着每次都完成上述判断，不意味着每张图都必须同时出现 Grid、透明背景和 inset。

## 下一阶段 Skill 分支：Pipeline Figure 协同设计

### 图型定位

Pipeline figure 是论文插图中的独立类型：它通常串联输入、中间表示、多个算法 module、分支/融合路径、训练目标和最终输出，有时还嵌入真实的中间结果。它既不是统计结果图，也不是单纯的 demonstration grid。

本分支的目标不是让 Agent 在信息不完整时独立猜测并交付“最终版 pipeline 图”，而是让 Agent 成为论文作者的**视觉头脑风暴与协同设计伙伴**。

### 核心交付原则：先给可讨论的草版，不冒充终稿

用户没有明确要求且关键信息尚未齐全时，首次交付必须标明为 `Draft / Concept / Wireframe`，并包含以下四部分：

1. **低保真视觉草版**：规划输入、模块、分支、中间结果、输出和说明文字分别放在哪里；明确主阅读方向与箭头连接关系。草版不能退化成“若干文字框的流程图”，必须为真实输入、关键中间结果和最终输出预留具有实际面积的图片槽位，让用户能直观看出后续素材将如何进入版面。
2. **结构清单**：用简短文字列出当前草版中的模块顺序、并行分支、融合点、反馈路径和训练/推理差异。
3. **待补内容清单**：在图中直接使用清楚的占位符，例如 `[请提供：中间特征图]`、`[待确认：模块名称]`、`[请提供：输出样例]`，同时在图外汇总缺失材料。
4. **下一轮高价值问题**：只询问会显著改变结构或视觉设计的信息，引导用户逐步补充，而不是一开始要求用户完整描述所有细节。
5. **可编辑主文件**：首次交付的主文件必须是可二次编辑的矢量格式；Figma 优先使用带命名分组的 SVG，必要时同时提供 PPTX。PNG 只作为快速预览，不能成为唯一交付物。

草版应帮助“脑中一片空白”的用户迅速获得一个可修改的起点；它不应暗示算法细节已经被 Agent 正确理解或最终视觉方案已经确定。

### 建议写入最终 Skill frontmatter 的触发语义

> Co-design preliminary academic pipeline, method-overview, model-module, and neural-network architecture figures. Use when a researcher needs a visual starting point but has incomplete modules, intermediate results, or layout ideas. Produce an explicitly labeled editable draft or wireframe with module placement, grouping, arrows, placeholders, assumptions, and a concise missing-input checklist; then guide iterative refinement. Do not invent algorithmic details or present the first draft as a publication-ready final figure.

### 首轮协同工作流

1. **提取已知叙事**：从用户材料中识别 problem、input、processing stages、branches、fusion、loss/objective 和 output。把“用户明确提供”“Agent 暂时推断”“仍然缺失”分开记录。
2. **先确定故事线**：选择左→右、上→下、双流汇合、encoder–decoder、循环迭代或分阶段训练等最合适的主结构。不要先沉迷颜色和装饰。
3. **给出一个主草案**：优先提供一个最有把握的 layout；若存在两种本质不同的叙事方式，最多再给一个简短备选，不一次堆出大量方案让用户选择。
4. **使用可替换占位符**：未知模块、中间结果、tensor shape、公式、图标和输出样例必须用视觉上明确的 placeholder 表示，不能虚构内容填满画面。
5. **规划箭头语义**：区分主数据流、skip connection、conditioning、监督信号和可选路径；优先减少交叉线，必要时使用分区、汇流节点或不同线型。
6. **标出用户补充点**：直接告诉用户应在哪些位置提供原图、中间 feature、模块内部结构、损失函数或真实输出，并说明每项材料会影响哪一部分设计。
7. **逐轮细化**：用户补充内容后再调整模块尺寸、信息密度、颜色、对齐、caption 和细节层级。颜色应按语义从全局 P1–P5 选择完整组合，不因这是 pipeline 就锁定 P4/P5。只有用户明确要求且内容完整时，才进入 publication-ready polish。
8. **执行外接框审计**：在导出前检查所有一级 scope 的顶部、底部和列间 gutter；没有叙事理由的一级容器应尽量共享上下锚点。局部高度不足时，优先扩展图片区、结果区或说明区来消化空间，而不是留下无法使用的大块空白。
9. **保留编辑语义**：SVG 中按 `input / module / result / connector / scope` 建立命名分组，并为每个待替换图片槽设置独立 group；不要把整张草图栅格化，也不要把所有元素焊接成一条难以选中的复合路径。

### Agent 不得擅自补全的内容

- 未经用户说明的算法 module、训练阶段或数据流；
- 猜测的 tensor shape、数学公式、loss 名称和中间变量；
- 伪造的生成结果、特征图、attention map 或定量结果；
- 为了让图显得“完整”而添加没有论文依据的支路、图标或装饰模块。

可以提出假设性方案，但必须显式写成 `Assumption` 或 `Option`，并让用户确认。

### 从后续 reference paper 中重点学习

1. 整幅图的阅读方向、视觉入口和故事节奏；
2. module 的形状、嵌套、分组、对齐与间距；
3. 主路径、分支、融合、skip connection 和反馈箭头的绘制方式；
4. 颜色如何编码阶段、数据类型、可训练/冻结模块或不同语义流；
5. 中间结果、输入输出样例、feature map 和公式如何嵌入 pipeline 而不打断阅读；
6. 大模块与局部放大结构之间如何建立视觉对应；
7. panel label、module label、caption、legend 和解释性 callout 的层级；
8. 如何在双栏/单栏论文宽度内控制复杂度和可读性。

未来提炼的是这些**可迁移的设计语法**，不是复刻参考论文的具体算法内容。

### 草版完成标准

- 用户能在几秒内看懂主要输入、处理方向和输出；
- 所有箭头都有明确起点、终点和语义，没有无法解释的连接；
- 已知内容、推断内容和待补内容视觉上可区分；
- 用户能准确知道下一步应提供哪些中间结果或算法信息；
- 草图在目标单栏/双栏画布中保持紧凑，没有因局部模块异常凸出而形成大片无法利用的留白；
- 一级 scope 的上下锚点和列间 gutter 已完成对齐检查；任何不对齐都具有明确叙事原因，而不是随意尺寸造成的空洞；
- 关键输入、中间结果和最终输出都有足够大的可替换图片槽，草图不是纯文字框堆叠；
- 草版以带命名图层/分组的 SVG 或等效矢量文件为主交付，便于在 Figma 中移动 module、替换 placeholder 和重新连接路径；PNG 只作预览；
- 阴影已经完成显式决策：只施加于关键前景 module 和主要结果卡片，scope 边界保持扁平；
- 在用户确认前不声称是最终图或 publication-ready 版本。

### 当前已整合的 Pipeline 稳定规则（V2 测试后）

1. **把 Agent 定位为版式协作者**：优先解决故事线、模块位置、图片槽位、分组与连接关系；没有真实中间结果时不冒充最终成图。
2. **先定主阅读脊柱，再安排支路**：根据方法选择左→右、上→下、双流汇合或分阶段训练；conditioning、loss、teacher 和局部说明尽量收进主结构已经形成的上下空间。
3. **用外接框审计约束紧凑度**：一级 scope 尽量共享顶部/底部锚点并保持稳定 gutter；任何局部突起或不对齐都必须有叙事理由。发现死空白时，优先扩大关键图片区或重新分配列宽，而不是增加无意义文字。
4. **把图片当作一等版式元素**：为输入、代表性中间结果和最终输出预留足够大的独立 replacement group；重复输入可以紧凑堆叠，关键结果才使用圆角、对比边框和轻阴影。
5. **用形状和效果编码层级**：逻辑 scope 使用扁平、浅色、虚线圆角框；具体 module 使用实线圆角卡；关键前景实体和主要结果卡使用一致的轻阴影。不要给每层嵌套容器都加阴影。
6. **按背景决定文字和边框对比度**：浅底使用深色字，深色或渐变 module 使用白字；图片边框和 caption 颜色根据图像明暗选择，必要时使用轻微底托或描边。
7. **让箭头承担语义而非装饰**：主数据流、监督信号、teacher/distillation 与可选路径使用稳定的颜色和线型组合；转角圆润，优先水平/垂直路由并减少交叉。
8. **默认交付可编辑矢量草案**：以带命名分组和独立 replacement groups 的 SVG 作为 Figma 优先主文件；PNG 只提供预览。用户补充素材后，在同一结构上继续替换图片、移动 module 和重连路径。

这些规则已经通过 AsyncEvGS V2 的正向测试获得初步认可，但仍属于可继续迭代的 pipeline 分支，不应写成唯一固定模板。

### Pipeline 的特殊子类型：Neural Network Architecture Figure

当用户需要绘制 transformer block、encoder-decoder、U-Net、backbone、feature pyramid、multi-branch network 或其他神经网络结构时，进入此子分支。它继承普通 pipeline 的紧凑布局、语义配色、圆角、箭头和可编辑 SVG 规则，但额外强调：

- tensor / token / feature map 的 shape、分辨率和 channel 变化；
- 重复 block、共享权重、`N ×` 结构和局部 block 放大；
- residual、skip、conditioning、concat、sum 与其他 merge operator；
- module 名称、shape metadata、数学符号和 panel caption 的独立文字层级；
- 主干连接线相对 module 边界的线宽层级。

首次参考案例为 Paper 02 Figure 3；当前规则 N01–N07 仍需更多网络结构图或一次正向测试验证。

### 与统计图 Skill 的路由关系

- 数据曲线、柱状、散点、误差和相关性 → 使用“学术统计图”分支并直接追求可发表质量。
- 算法总览、模型 module、训练/推理流程和多阶段 pipeline → 使用“Pipeline Figure 协同设计”分支，首次输出低保真草案与待补清单。
- transformer block、encoder-decoder、U-Net、feature hierarchy 或带 tensor shape / residual / skip connection 的结构 → 使用“Neural Network Architecture Figure”子分支。
- 生成、重建、NVS、rendering、point cloud 或 geometry 的结果与 baseline 对比 → 使用“Qualitative Demonstration Figure”分支。

## 新分支：Qualitative Demonstration Figure 协同设计

### 图型定位与协作边界

Qualitative demonstration figure 用于展示生成、重建、NVS、rendering、3D point cloud、mesh、depth、normal 或其他 geometry 结果。Agent 的职责是判断展示模态、规划行列语义、提供可编辑 layout 草案、检查公平性与一致性，并在用户提供素材后完成合成；案例的科学代表性和最终选择权属于用户。

Agent 不得用无关生成图片冒充用户模型的实验输出，也不得为了颜色好看擅自删除失败案例或改变 baseline 的原始结果。视觉建议必须服从科研真实性和公平比较。

### 首轮工作流

1. **先确认模态**：区分 2D raster、NVS/rendering、3D point cloud 投影、mesh/geometry、depth/normal 等；模态不同会改变相机、坐标轴、背景、裁切、光照和颜色规范。
2. **定义网格语义**：明确行和列分别编码 method、case、seed、view、time、scale、ablation 或其他变量；不能先画任意 grid 再硬塞内容。
3. **索取素材清单**：让用户提供候选 case、baseline、proposed result、输入/GT、必要标签以及希望强调的比较；先用可替换 placeholder 给出 layout。
4. **建立公平约束**：同一比较组保持一致的裁切、长宽比、分辨率、相机视角、坐标范围、背景、光照和后处理；任何例外都必须标注。
5. **给出内容选择建议**：可以建议在 case 之间建立色相、明度、场景类型与几何复杂度的差异，避免整页样例视觉上同质；但不能替用户决定科学代表性。
6. **素材到齐后再合成**：统一裁切、缩放、对齐、gutter、标签和导出；主交付保留可编辑布局，PNG/PDF 用于预览与论文提交。

### 初步完成标准

- 行列语义能在几秒内看懂，且无需为每个 tile 重复冗余标签；
- 所有 tile 的边界、行高、列宽和 gutter 完成像素级对齐检查；
- 相同比较组没有拉伸、非等比缩放、不同 crop 或隐蔽后处理；
- 案例集合在色相、明度、内容和难度上具有足够覆盖，同时不过度 cherry-pick；
- 2D、3D 与 geometry 模态使用各自合理且一致的观察条件；
- 用户可以在草案中直接替换 case、method 或结果，而不需要重新搭建整张 grid。

## Paper 01 — Diffusion Transformers with Representation Autoencoders

- arXiv：2510.11690v1
- 源文件目录：`reference papers/diffusion-transformers-with-representation-autoencoders/`
- 归档处理：原 `arXiv-2510.11690v1.tar.gz` 已通过完整性检查、成功解压并删除。
- 分析日期：2026-07-14

### Figure 与源文件映射

| 论文对象 | 源文件 |
|---|---|
| Figure 1 | `assets/teaser_data_v2.pdf` |
| Figure 2 | `assets/arch_teaser_v1.pdf` |
| Table 1 | `iclr2026_release.tex:163-264` |
| Figure 3 左/右 | `assets/model_width_2.pdf` / `assets/model_depth_2.pdf` |
| Figure 6A | `assets/ditdh_vs_ditxl.pdf` |
| Figure 6B | `assets/convergence_teaser_standalone.pdf` |
| Figure 6C | `assets/encoder_scaling_epoch80.pdf` |

### 用户明确偏好

1. Figure 1 在数值跨度较大时使用非均匀的纵轴刻度，使低值区域仍有足够的分辨空间。
2. Figure 1 使用上、下、左、右四条边框形成完整闭合画框，边界感比只保留左、下坐标轴更强。
3. Figure 2 的红蓝并非高饱和纯红、纯蓝，而是更柔和且经过调制的颜色。
4. Table 1 使用浅灰底色标记默认配置（如 DINOv2-B），灰色值得复用。
5. Figure 3 使用经过调制的红、绿、蓝、橙；区域背景使用透明色，使底层 Grid 保持可见。
6. Figure 6C 为不同模型系列选择了协调的橙、红、绿、紫、蓝色阶，应沉淀为常用科研绘图色板。
7. Figure 6B 的横轴刻度按数据和叙事需要灵活选择；同一模型的不同尺寸使用同色相的深浅变化来建立从属关系。

### 技术证据与候选规则

#### A01 — 大跨度数值采用对数轴与人工主刻度

- **技术证据**：Figure 1 不是任意扭曲刻度，而是对数纵轴。显示主刻度为 `1.2, 1.5, 2, 3, 5, 10, 20, 30`；等距位置表示相近的倍率变化，而不是相同的绝对差值。
- **候选规则**：当数值跨越约一个数量级以上，或低值区域的相对差异比高值区域的绝对差异更重要时，考虑使用 log 轴。不要依赖自动刻度；人工选择能支撑论文叙事的主刻度，并直接标出实际数值。
- **防误用**：必须在坐标含义上允许倍率比较；含零值、负值或强调绝对差值的数据不得直接套用 log 轴。
- **实现提示**：Matplotlib 可用 `ax.set_yscale("log")`，再显式设置 `1.2, 1.5, 2, 3, 5, 10, 20, 30`。
- **证据强度**：1/1，暂定。

#### A02 — 比较型 teaser 图默认使用完整画框

- **技术证据**：Figure 1 四条 spine 均存在，黑色，矢量线宽约 `0.8 pt`；Grid 为 `#B0B0B0`、约 `0.8 pt`。闭合画框清楚界定了长宽比较区域。
- **候选规则**：对散点比较、趋势比较和 teaser chart，默认保留四条 spine，除非完整边框明显增加拥挤或与后续证据冲突。
- **注意**：这是用户明确偏好的默认风格，但本论文 Figure 6 自身使用了只保留左、下 spine 的另一种风格。最终 Skill 应把“完整边框”写成强默认，而不是不分图型的绝对禁令。
- **证据强度**：用户强偏好；论文证据 1/1。

#### A03 — 避免原色，使用柔和但可区分的成对配色

- **技术证据**：Figure 2 的模块填色如下：

| 角色 | Hex | RGB | 备注 |
|---|---:|---:|---|
| VAE 红 | `#FB8E89` | `(251, 142, 137)` | salmon/coral 倾向，不是纯红 |
| RAE 蓝 | `#6F9AFE` | `(111, 154, 254)` | 柔和 cornflower blue，不是纯蓝 |
| 结构深灰 | `#595959` | `(89, 89, 89)` | 同时承担模块和描边，压住浅色填充 |

- **候选规则**：二元对比图避免 `#FF0000`/`#0000FF`。优先选择较高明度、适中饱和度的暖珊瑚红与冷矢车菊蓝，并配统一深灰描边建立结构。
- **证据强度**：1/1，暂定色板。

#### A04 — 表格用极浅中性灰标记默认配置

- **技术证据**：Table 1 使用 LaTeX `\rowcolor{gray!20}`。标准 `xcolor` 混色在白底上的有效颜色约为 `#E6E6E6`（90% white / 10% black）。它标记“默认设置”，而不是标记最佳结果；最佳结果仍可用 bold 表示。
- **候选规则**：表格需要标记默认、选中或参考配置时，使用 `#E6E6E6` 的整行/整格浅灰底；不要用高饱和颜色抢夺数值本身的视觉层级。用底色表达“配置身份”，用粗体表达“数值优胜”，避免语义混用。
- **证据强度**：1/1，暂定。

#### A05 — 区域着色保持 Grid 可见

- **技术证据**：Figure 3 的关键颜色为：

| 角色 | Hex | Alpha | 备注 |
|---|---:|---:|---|
| 理论曲线红 | `#F5433D` | 1.00 | 偏珊瑚的强红 |
| 观测点绿 | `#88B06D` | 1.00 | 柔和草绿 |
| 左侧风险区 | `#F5433D` | 0.15 | 极浅粉红背景 |
| 右侧成功区 | `#5D8DFD` | 0.15 | 极浅蓝背景 |
| Grid | `#D3D3D3` | 1.00 | 中性浅灰 |
| 橙色说明框 | `#EF9463` | 约 0.60 | 描边 `#C46032` |
| 蓝色说明框 | `#002FAB` | 约 0.30 | 描边 `#496EC8` |

- **候选规则**：用背景区域编码状态时，优先复用相应曲线/类别的主色并将 alpha 控制在约 `0.10–0.18`；让 Grid、数据点和注释始终高于背景层。注释框可采用更高 alpha（约 `0.3–0.6`）并增加同色系深描边。
- **证据强度**：1/1，暂定。

#### A06 — Figure 6 科研绘图五色、三级色阶

Figure 6C 的每个气泡都使用 `alpha=0.75`。同一模型家族由浅、中、深三个明确 RGB 色值构成，而不是只靠单一颜色变化。

| 系列 | 浅色 | 中色 | 深色 | Alpha |
|---|---:|---:|---:|---:|
| MDTv2 / 橙 | `#F9CB8A` | `#F7BA64` | `#F5A83D` | 0.75 |
| REPA / 红 | `#FBA09D` | `#F86762` | `#F5433D` | 0.75 |
| DDT / 绿 | `#B3CDA2` | `#9EBF88` | `#88B06D` | 0.75 |
| REG / 紫 | `#D0B3FF` | `#A984E6` | `#7A5DE1` | 0.75 |
| DiT-DH / 蓝 | `#AEC6FE` | `#86AAFE` | `#5D8DFD` | 0.75 |

- **候选规则**：把这 15 个颜色作为候选常用科研色板。跨模型用色相区分；同一模型的 scale/size 用浅→深的顺序色阶区分；气泡图或存在重叠的面积标记使用 `alpha≈0.75`，让重叠关系可见。
- **防误用**：小尺寸折线图一次不应使用全部五个家族和三级色阶。只抽取任务所需的最小子集，并同时依靠线型、marker 或直接标注保证灰度打印可辨识。
- **证据强度**：1/1，暂定色板。

#### A07 — 灵活刻度与同色系层级

- **技术证据**：Figure 6A/6B 的训练 FLOPs 横轴使用 log scale，并只标出叙事需要的少数主刻度；例如 Figure 6B 显示 `10^11` 和 `5×10^11`，同时保留较短的 minor ticks。
- **候选规则**：计算量、参数量、吞吐量等跨倍率横轴使用 log scale，并人工筛选 2–4 个可读主刻度；保留不带标签的 minor ticks 帮助估计位置，避免自动刻度制造密集科学计数法标签。
- **证据强度**：1/1，暂定。

### 重要技术修正：透明度与浅色阶不是同一件事

用户正确识别到了 Figure 6B 中“同一语义家族使用深浅差异”的设计意图，但 PDF 矢量对象显示：Figure 6B 的曲线和点均为 `alpha=1`，采用预先计算好的浅色与深色，例如蓝色 `#AEC6FE` / `#86AAFE` / `#5D8DFD`。真正使用透明度的是 Figure 6C（所有气泡 `alpha=0.75`）和 Figure 3 的区域背景（`alpha=0.15`）。

因此，候选 Skill 规则应区分：

- 用**固定浅/中/深 RGB 色阶**表达同一模型的尺寸层级；它在白底、彩底和导出格式之间更稳定。
- 用**alpha**表达背景区域、置信带或对象重叠；它允许 Grid 和下层对象透出。
- 不要把降低 alpha 当成所有“浅色”的默认实现，否则同一曲线会随背景颜色改变外观。

### 暂不进入 Skill 的观察

- Figure 1 嵌入 Times New Roman；Figure 2 嵌入 Google Sans Code；Figure 6C 主要使用 Arial/DejaVu Sans。用户本轮没有把这些字体列为喜欢的点，因此只保留为来源事实，不把它们升级为字体规范。
- Figure 6C 隐藏上、右 spine，与 Figure 1 的完整画框偏好相反。等待后续论文确认不同图型应采用哪种边框策略。

### 本篇论文后的暂定风格方向

1. 对数轴必须服务于倍率关系和低值分辨率，并配人工主刻度。
2. 比较型 teaser chart 强默认使用完整画框。
3. 避免纯红、纯蓝、纯绿；优先使用本篇提取的柔和科研色板。
4. 区域底色使用低 alpha，数据对象使用实色或稳定的预调色阶。
5. 表格默认配置用 `#E6E6E6`，最佳数值用粗体，二者语义分离。
6. 每条规则目前只有一篇论文证据，继续等待后续 4–9 篇论文校正。

## Forward Test 01 — 三张合成论文图（用户整体通过）

- 测试日期：2026-07-14
- 渲染脚本：`scripts/render_skill_test.py`
- 输出目录：`output/skill-test/`

| 测试图 | 验证规则 |
|---|---|
| `01-benchmark-teaser` | log 纵轴、人工主刻度、四边完整画框、灰蓝主次层级、直接标注 |
| `02-regime-map` | 红蓝区域 `alpha=0.15`、Grid 穿透、红色虚线、绿色观测点、半透明说明框 |
| `03-scaling-bubbles` | 五组三级色板、气泡 `alpha=0.75`、同色系尺寸层级、log 纵轴、人工刻度 |

### 用户评价

- 用户确认三张图整体上在字体、配色、边框和标注方面表现不错。
- 用户认为对 Paper 01 的视觉规律学习效果很好。
- 本次测试因此从“等待评价”升级为“首次合成迁移测试通过”。它证明当前规则可以用于重新绘制新数据，而不只是描述或复刻参考图；仍需后续论文和不同图型继续检验泛化性。

### 原创性核验

- `scripts/render_skill_test.py` 不读取 `reference papers/`、论文 `assets/` 或任何图片文件；所有测试数据均直接定义在脚本中。
- 三份测试 PDF 的 `pdfimages -list` 均无图像条目，输出由 Matplotlib 矢量路径、文字和 marker 构成，没有嵌入论文原图或其他栅格图。
- 测试借鉴的是 Paper 01 中提取出的视觉规则和精确色板，而不是复用其 Figure 内容。

## Paper 02 — Scalable Diffusion Models with Transformers

- arXiv：2212.09748v2
- 源文件目录：`reference papers/scalable-diffusion-models-with-transformers/`
- 归档处理：原 `arXiv-2212.09748v2.tar.gz` 已通过完整性检查、成功解压并删除。
- 源码清单：39 个文件，其中 `figures/` 下有 14 个矢量 PDF。
- 分析状态：统计结果图（Figure 2、Figure 9、Figure 12）的审美提炼与局部放大正向测试已完成；现新增 Figure 3 作为“神经网络架构图”子分支的首个参考案例。

### 主要 Figure 与源文件映射

| 论文对象 | 源文件 | 内容 |
|---|---|---|
| Figure 1 | `figures/teaser_v2.pdf` | 512/256 生成样例 teaser |
| Figure 2 | `figures/teaser_new.pdf` | DiT scaling 气泡比较 |
| Figure 3 | `figures/block.pdf` | DiT 架构与 conditioning block |
| Figure 4 | `figures/patches.pdf` | patchify 示意图 |
| Figure 5 | `figures/conditioning.pdf` | conditioning 策略曲线 |
| Figure 6 | `figures/scaling_new.pdf` | 12 个 DiT 模型 scaling 曲线 |
| Figure 7 | `figures/visual_scaling_new.pdf` | 视觉质量随算力扩展 |
| Figure 8 | `figures/gflops-FID-50K.pdf` | Gflops 与 FID 相关性 |
| Figure 9 | `figures/training-complexity-FID-50K-inset.pdf` | 总训练算力与 FID |
| Figure 10 | `figures/sample_complexity_new.pdf` | sampling compute 对比 |

附录还包含 `training-complexity-all-metrics-inset.pdf`、`train_loss.pdf` 和额外生成样例。

### 本轮分析范围：统计结果图与集中展示图分流

- **统计结果图**：曲线图、柱状图、散点图、气泡图等，用于表达实验数据、趋势、相关性和比较关系。本轮提炼的边框、Grid、局部放大、紧凑排版与图内标注规则属于这一分支。
- **集中展示图（Demonstration）**：展示生成结果、重建结果或与 baseline 的视觉对比。它需要另一套关于样例选择、裁切、对齐和标签的规则，本轮不从 Figure 1 等展示图外推。
- **候选 Skill 路由规则**：Agent 开始作图前先判断图型；不要把统计图的坐标轴规范机械套到 demonstration grid，也不要用展示图的无坐标布局处理统计结果。

### 用户明确偏好

1. Figure 2 的柔和科研配色与 Paper 01 相近；统计图保留上、下、左、右四条边框，并对重要 caption 或总结性标注选择性加粗。
2. Figure 9 在曲线拥挤处使用局部放大图：主图画出被放大的小框，建立主图与 inset 的空间对应；inset 的刻度、边框和位置需要单独设计，不能遮挡核心曲线或 legend。
3. Figure 12 采用高密度但不拥挤的多行两列 layout；行、列间距很小，左列明显宽于高且承担主要曲线，右列更窄、承担相关性摘要。
4. 少量短标注若能避开数据，应放在图内并保持对齐，优先使用图内空间而不是增加图外留白；标注多、文字长或必然遮挡数据时再放到图外。

### Figure 3 — 神经网络架构图子分支

源文件：`figures/block.pdf`。论文使用 `figure*` 并按 `width=\linewidth` 放置，原始矢量画布约为 `1656 × 684 pt`，宽高比约 `2.42:1`；它是双栏长条布局的成功实例，不是所有网络结构图必须使用的固定比例。

#### N01 — 先建立对齐的宏观 panel，再压紧 panel 内部模块

- **用户证据**：整图几乎占满双栏矩形画布，没有大片无意义留白。
- **技术证据**：左侧完整 Latent Diffusion Transformer 与右侧三个 DiT block 变体共同组成横向长条；三个 block panel 的顶部、底部、宽度和下方标题基线高度高度一致。模块沿清晰的纵向主脊柱堆叠，residual 与 conditioning 支路被收进 panel 内部，没有为了支路任意扩大外接框。
- **候选规则**：先确定目标单栏/双栏宽高比、宏观 panel 数量、共享顶底锚点和标题基线，再布置 panel 内 module。重复 block 应共享外框尺寸、内边距和纵向节奏；只有内容确实不同才允许局部高度变化。
- **防误用**：紧凑不等于取消必要间距。主脊柱、残差回路、条件输入和 panel 标题之间必须保留稳定 gutter；需要消除的是死空白，而不是所有空白。

#### N02 — 字号必须服从模块尺寸和信息角色

- **用户证据**：`DiT Block`、`Scale`、`Pointwise Feedforward` 等文字与各自圆角矩形的尺寸匹配；不存在统一字号硬塞进不同大小模块的问题。
- **字体核验**：PDF 嵌入了 Helvetica、ArialMT、Avenir-Book 与 Cambria Math。Poppler 提取到的相对字号层级为：左侧主要 module label 约 `42`、panel 标题约 `36`、block 内部 label 约 `27`、tensor shape 约 `27`、`N ×` 重复标记约 `54`；数值受提取缩放影响，但比例关系可靠。
- **候选规则**：网络架构图使用 3–4 个稳定文字层级，并允许同一层级按 box 宽度小幅调整。先保留左右内边距和上下呼吸空间，再决定字号；不要让文字贴边，也不要为了统一字号把短标签缩得空洞。
- **实现检查**：在最终论文缩放尺寸检查最长标签；必要时先换行或扩大 module，再缩字号。不同 panel 中的同类 module 仍应保持相近字号，不能每个框独立自动缩放到毫无体系。

#### N03 — 主标签、tensor shape 与数学变量使用不同文字语法

- **用户证据**：`32 × 32 × 4` 等 shape 信息与主要 module 名称在字体和视觉权重上明显不同，读者可以快速区分“操作”与“元数据”。
- **技术证据**：主 module 多使用 Helvetica，tensor shape 与 `N ×` 标记使用 Avenir-Book，希腊字母和上下标使用 Cambria Math；shape 字号约为主要 module label 的 `0.64`。
- **候选规则**：module 名称使用主 sans-serif；tensor shape、token 数、分辨率和 channel 数使用更小、更轻的 secondary style，并固定放在 module 内下方或紧邻输出端；数学符号使用兼容的 math font。不要把 shape 做成与 module 名称同等醒目的标题。
- **防误用**：这里学习的是“信息角色分层”，不是强制混用四种字体。实际绘图可用一个主字体家族的 regular/medium 与 math companion 实现，只要 shape 和主标签有稳定差异。

#### N04 — DiT Figure 3 的柔和彩色 module 调色板

| 视觉角色 | 矢量 PDF 精确色值 | Figure 3 中的典型用途 |
|---|---:|---|
| 柔和蓝 | `#C6DBFE` | Layer Norm、Scale/Shift、Embed、Conditioning |
| 柔和绿 | `#C3E3BD` | Pointwise Feedforward、Linear and Reshape |
| 柔和橙 | `#F9CC8B` | Multi-Head Self-Attention |
| 柔和红 | `#FBA09E` | Multi-Head Cross-Attention |
| 中性灰 | `#D3D7E3` / `#D4D7E3` | latent、input token、noise、prediction |
| 近白灰 | `#F3F3F6` | 大 block panel 背景 |

- **用户证据**：红、蓝、橙、绿组合获得明确认可。
- **候选规则**：先按操作语义分配颜色，再在全图保持一致：normalization/affine 可用蓝，MLP/feedforward 可用绿，attention 可用橙，额外或特殊 attention 可用红，tensor/data object 可用灰。颜色是语义编码，不是随机轮换。
- **跨分支关系**：本组色值与全局柔和统计图色板非常接近，可纳入全局 palette family；在网络架构图中使用较大面积的浅色填充，在统计图中可选择更深同系色作为线与 marker。
- **防误用**：不要求每张网络图同时出现四种颜色。模块语义不足四类时应减少颜色；同一语义不得在不同 panel 中随意换色。

#### N05 — 圆角半径按层级成组，不对所有框使用同一个半径

- **用户证据**：所有 module 使用圆角矩形，避免生硬直角。
- **技术证据**：内部短条 module 使用较小圆角；较高的 attention/feedforward 卡片使用更大的圆角；三个完整 block panel 使用显著更大的外轮廓圆角。彩色内部 module 主要依靠填充建立边界，不使用沉重黑框。
- **候选规则**：建立小 module、中等 operation card、宏观 block panel 三档圆角；同档保持一致。外层 block 可用更大半径建立包裹感，内部 module 保持较小半径以提高密度。
- **防误用**：圆角不能损害 tensor 形状或算子语义；卷积核、feature map、矩阵等需要表达几何形状时，不应全部改成相同卡片。

#### N06 — 箭头要比 module 边界更具有方向性

- **用户证据**：箭头明显比矩形边框更粗，流程指向性强。
- **技术证据**：主路径和 residual 路径使用黑色实线与实心三角箭头；彩色内部 module 多为无重边框填充，宏观 block 边界较细，因此连接线在视觉上更突出。residual 连接采用规整的水平/垂直折线，`+` 使用圆形节点，conditioning 从右侧进入，主 token 流自下而上。
- **候选规则**：网络架构图中让箭头线宽高于普通 module stroke，推荐从 `1.3–1.6×` 的视觉比例起步，并配合统一实心箭头头部。残差连接使用正交折线和独立 `+`/merge node；conditioning 从固定侧边进入，避免与主干混淆。
- **检查项**：箭头不得穿过文字；arrowhead 大小要与线宽同步；多个 block panel 中同类路径应保持相同粗细、转角和入口位置。

#### N07 — 当前神经网络架构图的初步完成标准

1. 宏观 panels 的外接框、顶底锚点、caption baseline 与 panel gap 已完成对齐审计；
2. module 字号按 box 尺寸和信息角色调整，并在最终论文缩放尺寸下仍可读；
3. tensor shape、分辨率、token 数和数学变量与主要 module 名称视觉分层；
4. 颜色按算子语义稳定映射，不使用随机彩虹色；
5. 圆角按 module / operation card / block panel 三档组织；
6. 主流、residual、conditioning 和 merge node 的箭头语义清楚，线宽层级高于普通 module 边界；
7. 首次草图仍优先交付可编辑分组 SVG，并为用户保留修改 module、shape 和连接关系的能力。

以上 N01–N07 来自单篇 Figure 3 与用户明确评价，先作为神经网络架构图子分支的高优先级候选规则；等待后续网络结构图或正向测试验证后再升级为强默认。

### Figure 7 — 2D 生成结果的高密度展示矩阵

源文件：`figures/visual_scaling_new.pdf`。画布约为 `1634 × 2038 pt`，呈接近整页的纵向双栏版式。PDF 内嵌 15 张 `1064 × 800` JPEG case sheet，每张 case sheet 本身包含 `4 列 × 3 行` 的结果；整页由 `3 个 case × 5 个横向 setting band` 组成，因此总计 180 个方形结果 tile。

#### Q01 — 画 demonstration figure 前先做 modality audit

- **用户规则**：首先确认展示对象是 2D image、NVS/rendering、投影后的 3D point cloud、带 XYZ 轴的 3D plot，还是其他 geometry modality。
- **候选工作流**：
  - 2D image / NVS / rendering：统一 crop、长宽比、分辨率和颜色空间，禁止拉伸；
  - 3D point cloud：统一 camera pose、projection、axis range、point size、background 和视锥；
  - mesh / geometry / depth / normal：统一 viewpoint、lighting、material、colormap、range 和坐标约定；
  - 混合模态：先分 panel，再建立清楚的视觉对应，不能把不同观察条件的结果直接当作同质 tile 比较。
- **协作边界**：Agent 先询问模态和比较目的，再给草版；不能在不知道结果语义时直接选择 grid 模板。

#### Q02 — 使用“嵌套网格”同时表达 case 与 setting

- **用户证据**：每个横向 band 包含三个 case，每个 case 内部通过三行表示 patch size 变化，并通过四列表示 transformer size 变化。
- **技术证据**：15 个 case sheet 以三列、五个 band 排列。每个 sheet 在 PDF 中约为 `532 × 400 pt`；相邻 sheet 的外部间隔接近零，视觉分隔主要来自 contact sheet 内部统一的白色 gutter。所有 band 的列起点与行起点完全复用。
- **候选规则**：当展示同时包含 case 与两个实验变量时，优先把每个 case 组织成固定规格的 mini-grid，再把 mini-grid 作为整体放进宏观 grid。不要把 180 个 tile 当作一个没有层级的扁平矩阵。
- **防误用**：嵌套层级必须服务真实变量。若只有 method × case 两个维度，就使用普通二维矩阵，不为追求复杂感添加空的内层网格。

#### Q03 — 对齐和 gutter 是定性展示图的硬约束

- **用户证据**：行、列必须严格对齐，所有横向和纵向间距完全一致。
- **技术证据**：case sheet 的 x 起点约为 `40.62 / 572.77 / 1104.92 pt`，y 起点约为 `37.86 / 437.91 / 837.95 / 1237.95 / 1637.95 pt`；相邻 case sheet 的间隔仅约 `0.05–0.15 pt`。单个 sheet 为 `4 × 3`、接近方形 cell 的规则矩阵。
- **候选规则**：使用统一 cell size、row height、column width 与 gutter token；所有 tile 采用同一裁切策略。导出前检查首末边界、每条分隔线和累计误差，避免最后一列或最后一行逐渐漂移。
- **实现提示**：先用整数像素确定 tile 和 gutter，再整体缩放到论文宽度；不要在最终 PDF 尺寸中逐格手工拖动，因为小误差会累积。

#### Q04 — 重复的变量说明只标一次

- **技术证据**：`Increasing transformer size` 只在顶部用一条水平箭头说明，`Decreasing patch size` 只在左侧用一条垂直箭头说明；180 个 tile 没有重复添加相同标签。
- **候选规则**：当所有 mini-grid 共享相同行列语义时，使用一次全局方向标注或共享 header/side label。只有某个 group 的设置不同，才增加局部 label。
- **收益**：减少文字占用，让图片本身成为主体，同时维持紧凑整页 layout。

#### Q05 — 案例选择应同时考虑色相与明度构图

- **用户证据**：
  - 第一组代表性 case 形成橙 / 绿 / 蓝对比；
  - 中间组形成绿 / 黄 / 红对比；
  - 后续组形成蓝 / 白 / 黑等强明度与色相对比。
- **候选建议**：在科学代表性成立的前提下，从候选池中选择主色、背景明度和场景内容具有差异的 case，使相邻大 case 不会全部落在同一色域。可以主动提醒用户避免整页全白、全黑、同一背景或相近主色。
- **建议工具化**：素材到齐后，Agent 可以生成缩略图 contact sheet，并计算平均色相、饱和度、明度或简单的感知距离，作为排序建议；最终案例仍由用户确认。
- **科研约束**：颜色构图只能作为同等科学有效候选之间的选择因素，不能覆盖难例、失败模式、类别覆盖和公平性，也不能通过调色改变模型输出。

#### Q06 — Agent 先给 layout storyboard，再等待真实结果

- **用户规则**：Agent 不应独立假定并交付最终案例集合；先给包含 case、setting、行列变量和标签位置的草版，用户提供或确认原材料后再合成。
- **草版要求**：placeholder 必须标出 `[case A]`、`[method / size / view]`、行列方向和预期 crop；如果每个 case 内还有多种设置，应画出真实数量的 mini-grid，而不是只写一段文字。
- **素材到齐后的职责**：统一裁切、对齐、gutter、标签、颜色管理与导出；若发现尺寸、视角或后处理不一致，应先报告而不是静默修补。

### Figure 11 与 Figure 14 之后 — 混合尺寸拼贴与补充材料结果页

Figure 11 的源文件为 `figures/teaser_v3.pdf`，画布约 `767 × 511 pt`。其中上排由 3 张 `512 × 512` 图组成；下方两排各由 6 张 `256 × 256` 图组成。PDF 以约 `144 ppi` 放置这些图，因此每张上排图约占 `256 × 256 pt`，每张下排图约占 `128 × 128 pt`：上排一张图精确跨越两个基础列，每一行的总跨度都等于六个基础列，最终形成没有闲置空洞的完整矩形。

Figure 14 开始的补充材料结果图则采用另一种紧凑模板：每张 `960 × 2048 px` 的纵向 contact sheet 以 `width=\linewidth` 放入单栏，内部图块大小不完全相同，却通过共享边界的 mosaic 铺满固定外接矩形。正文与补充材料共同说明，“紧凑”是外接框利用率和几何秩序，不等同于“所有图片必须同尺寸”。

#### Q07 — 混合尺寸结果先定义基础网格，再允许整数跨列

- **用户证据**：Figure 11 上方三张图的总宽度与下方每排六张图的总宽度完全一致；若上排较窄，左右就会产生难看的无效留白。
- **技术证据**：Figure 11 的尺寸关系严格满足 `512 = 2 × 256`。以 `256 px` 为基础单元时，下方每张占 `1 × 1` 单元，上方每张占 `2 × 2` 单元；三行均占六个基础列，左右边界完全对齐。
- **候选规则**：遇到不同分辨率、不同重要性或不同展示尺度的结果时，先建立最小 cell 与列数，再让大图跨 `2/3/...` 个整数单元。每一行的 span 总和必须相等；禁止靠肉眼拉宽、额外 padding 或不对称外边距补齐。
- **适用范围**：该规则既可用于“重点案例 + 更多小案例”，也可用于输入、reference、prediction 和局部 crop 的混合展示；前提是尺寸差异有清楚语义，不应无理由随机放大某些结果。

#### Q08 — “紧凑”是硬约束，“零间距”只是可选样式

- **用户规则**：图片之间可以无缝，也可以保留缝隙或增加边框；无论采用哪一种，最终 layout 都必须工整、对齐、紧凑，不能在 bounding box 内出现大片无意义空白。
- **候选决策**：
  1. **无缝拼接**：画面自身边界清楚、需要最大化展示面积、相邻 tile 不易混淆时使用；
  2. **统一 gutter**：需要帮助读者区分方法、视角或 case，或相邻画面颜色容易融合时使用；
  3. **细边框**：图像背景与页面背景接近，或不同 tile 的边缘色高度相似时使用。
- **一致性要求**：同一比较层级只使用一套 gutter / border token；所有行列间距、外边距和边框线宽必须一致。不能出现局部随意加宽的缝隙，也不能用空白代替真实的分组语义。
- **审计项**：检查最左/右边界、每一行总宽、行高、分隔线连续性、孤立空 cell，以及裁切后主体是否仍完整；紧凑不得以拉伸图片或裁掉科学证据为代价。

#### Q09 — 规则网格与异尺寸 mosaic 是两类模板

- **规则网格**：适用于 method × case、view × method 等严格比较。tile 尺寸、crop、gutter 和标签位置必须一致，便于逐行逐列比较。
- **异尺寸 mosaic**：适用于同一类别的大量样本、代表性展示或需要建立主次节奏的结果页。图块可以大小不同，但必须使用可求解的网格/treemap 约束填满外接矩形，不能形成不可解释的凹凸轮廓或内部孔洞。
- **补充材料一致性**：Figure 14 之后的结果页把每张 contact sheet 固定为相同的 `960:2048` 外形并铺满单栏宽度。Skill 应把单栏/双栏宽度、外接框比例和页面间一致性视为模板 token；不能每一页临时换一种宽度与边界。
- **科研提醒**：异尺寸 mosaic 会改变视觉权重。若不同 method 正在做公平对比，必须给它们相同面积；只有在同类样本展示或明确标注“重点案例”时才允许不等面积。

#### Q10 — 是否在图内放文字取决于比较任务，不由参考图机械决定

- **用户规则**：Figure 11 图内没有文字，不代表 demonstration figure 永远不应有文字。NVS 等任务常需标注 PSNR、SSIM、LPIPS、view id 或 method 名。
- **候选规则**：仅保留帮助读者定位或比较的最小文字。共享的 method / setting 优先使用一次性行列 header；逐图指标可以放在每张图内固定角落，或使用高度固定的紧凑 caption strip，但不能为少量文字在整行之外制造大块空白。
- **图内标注规范**：位置、字号、颜色、背景方式、指标顺序与小数位数全部一致；亮图用深字，暗图用浅字，复杂背景可加小面积半透明底或轻描边。标注不得覆盖主体、误差区域、遮挡关系或需要比较的纹理。
- **信息密度上限**：若每个 tile 的文字多到影响图像，应把共性信息移到共享 header、legend 或正式 figure caption，而不是继续缩小字号。

#### Q11 — demonstration layout 的几何完成标准

首次草版和最终合成都必须通过以下检查：

1. 先声明目标版面是单栏、双栏还是整页，并固定最终宽高或外接框比例；
2. 每一行的总宽度一致，最左和最右边界对齐；混合尺寸图块必须落在同一基础网格；
3. bounding box 内不存在无语义的大块空白、孤立空 cell 或突然凸出的模块；
4. gutter、border 与外边距采用成组 token，不能靠逐张手调制造伪对齐；
5. 所有图像保持正确长宽比；必要裁切应使用一致规则且不损伤科学内容；
6. 文本是可选信息层：需要时紧凑、对齐、高对比，不需要时不为装饰强加标签；
7. 最终在论文实际缩放尺寸下复检主体可见性、指标可读性和整页视觉平衡。

以上 Q01–Q11 是 Qualitative Demonstration Figure 分支的第一组高优先级候选规则。Figure 7、Figure 11 与 Figure 14 之后的补充材料共同验证了 2D 生成图片的规则网格、整数跨列和异尺寸满铺三种布局；3D、NVS 与 geometry 的具体视觉规范仍需后续案例补充。

### 技术证据与候选规则

#### B01 — 统计图先建立统一的基础视觉骨架

- **技术证据**：Figure 2、Figure 9 和 Figure 12 的统计坐标轴都保留四条黑色 spine。Figure 2 的 spine 约 `0.783 pt`，Figure 9/12 约 `0.8 pt`；Grid 均为 `#D3D3D3`，约 `0.5 pt`。
- **候选规则**：统计结果图默认采用白底、浅灰 Grid、四边闭合画框。推荐起点为 `spine=0.8 pt`、`grid=0.5 pt`、`grid_color=#D3D3D3`；数据曲线与 marker 必须处在 Grid 上层。
- **防误用**：这是一致性很高的默认骨架，不是绝对禁令。极小型 sparkline、无坐标展示或边框造成明显视觉噪声时可以例外，但 Agent 应说明例外原因。
- **证据强度**：Paper 02 内 3/3；结合 Paper 01 的 Figure 1，跨论文 2/2，升级为强默认。

#### B02 — Figure 2：复用稳定色板，层级不只依靠粗体

Figure 2 的 12 个彩色气泡与 Paper 01 Figure 6 的橙、红、绿、蓝四组三级色阶**逐个 Hex 完全一致**：

| 系列 | 浅色 | 中色 | 深色 |
|---|---:|---:|---:|
| 橙 | `#F9CB8A` | `#F7BA64` | `#F5A83D` |
| 红 | `#FBA09D` | `#F86762` | `#F5433D` |
| 绿 | `#B3CDA2` | `#9EBF88` | `#88B06D` |
| 蓝 | `#AEC6FE` | `#86AAFE` | `#5D8DFD` |

- **技术证据**：Figure 2 的气泡为 `alpha=1`，明暗层级来自预先调好的 RGB 色阶，而不是透明度；baseline 使用 `#BFBFC5` 和 `#D4D4D8`，重点 DiT 点使用深蓝 `#5D8DFD`。PDF 嵌入 Helvetica。
- **标注事实**：LaTeX 中 Figure 2 caption 的开头使用 `\textbf{...}`；图内模型名和底部总结标签通过字号、颜色、位置建立层级。PDF 字体信息只确认 Helvetica regular，因此不能把所有图内标签都误记为“实际使用了粗体”。
- **候选规则**：把以上四组色阶升级为常用统计图色板。baseline 使用中性灰，proposed method 使用色板中最深、辨识度最高的颜色。重要 caption 的首句、panel 总结或关键结论可选择性加粗；tick label、所有点名和全部正文不应一律加粗。
- **证据强度**：相同色板跨论文 2/2，已通过一次合成迁移测试，升级为高优先级候选色板。

#### B03 — Figure 9：局部放大必须同时表达“来源、层级、位置”

- **术语**：这里的目标是把局部区域放大，Skill 中统一称为 **zoomed inset / 局部放大图（zoom-in）**，避免把它写成 zoom-out。
- **技术证据**：主图用一个矩形标出 ROI，并用两条连接线指向 inset。主图与 inset 的 spine 都约为 `0.8 pt`；ROI 框与连接线约为 `1.0 pt`、黑色、`alpha=0.5`。因此视觉区分来自“稍粗但更淡的定位线 + 独立小坐标系”，而不是实际加粗 inset 边框。
- **尺寸证据**：inset 约占主坐标区宽度的 `37%`、高度的 `40%`。它位于主图右上区域、legend 下方，避开了最关键的数据聚集区，同时保留 legend。
- **刻度与 Grid**：inset 使用更少、更小的刻度标签；Grid 与主图同为 `#D3D3D3`、约 `0.5 pt`，维持同一视觉语言。
- **候选规则**：仅在关键曲线确实挤在一起、且局部差异支撑结论时使用 inset。实现顺序为：
  1. 在主图精确画出 ROI；
  2. 用 1–2 条低透明度连接线建立对应关系；
  3. inset 使用独立的 axis limits、较少刻度与较小字号；
  4. 在候选角落中选择数据最稀疏的位置，并显式检查 legend、关键曲线、峰值和注释的遮挡；
  5. 若四个角落都拥挤，优先把 inset 放到坐标区外或重新规划 layout，而不是遮住核心证据。
- **防误用**：不要为了装饰加入 inset；不要只放放大图却不在主图标 ROI；不要默认把 inset 四条边框加粗。
- **证据强度**：论文证据 1/1，且已通过一次合成数据正向测试；位置与尺寸仍需按具体数据自适应。

#### B04 — Figure 12：非对称双列 layout 服务信息密度

- **技术证据**：Figure 12 是五行两列的统计图矩阵，另在左上 panel 内含一个 inset。左列坐标区宽约 `431.13 pt`，右列约 `185.20 pt`，宽度比约为 `2.33:1`；左列单图宽高比约 `2.98:1`，接近 `3:1`。
- **间距证据**：两列坐标区间隔约 `27.87 pt`，约为整页宽度的 `4.1%`。左列相邻行的坐标区间隔约 `9.14 pt`，右列约 `3.96 pt`；均显著小于单个 panel 高度。上方四行压缩重复的横轴文字，只在需要处保留共享信息。
- **结构含义**：左侧宽图承载多条训练曲线与时间演化，右侧窄图把同一行压缩成相关性散点摘要。列宽不是追求机械对称，而是按信息量分配。
- **候选规则**：多行复合图先按内容密度确定 `width_ratios`，不要默认 `1:1`。当左列为长程曲线、右列为摘要散点时，可从 `2.3:1` 起步；左侧曲线 panel 可从约 `3:1` 的宽高比起步。共享 x 轴时，非底行隐藏重复 x tick labels，并把行距压到“不发生文字碰撞”的最小值。
- **实现提示**：Matplotlib 可使用 `GridSpec(..., width_ratios=[2.3, 1], hspace≈0.05–0.10, wspace≈0.12–0.18)` 作为起点，随后必须按实际字号和标签长度视觉校正，而不是把数值写死。
- **证据强度**：1/1，暂定布局模板。

#### B05 — 少量摘要文字优先放在图内的稳定空区

- **技术证据**：Figure 12 右列五张图分别将 `Correlation: -0.93`、`-0.86`、`0.90`、`0.93`、`0.86` 放在各自坐标区内部、靠近下方中央，并在五行保持一致对齐；没有为它们增加额外标题行。
- **候选规则**：每个 panel 只有 1–2 条短摘要、且存在稳定空区时，使用 axes-relative 坐标放在图内。下方居中可从 `x≈0.5, y≈0.03–0.08` 起步，跨 panel 保持同一锚点、对齐和字号；文本应避开数据、误差带、legend 和轴标签。
- **升级条件**：如果文字较长、条目较多、不同 panel 的空区不一致，或内部放置会遮挡关键数据，则改用图外 caption、统一 legend、表格式侧栏或额外行。
- **证据强度**：1/1；用户明确偏好，等待更多多面板论文验证。

### Paper 02 对当前 Skill 的更新

1. **完整四边框**由单篇观察升级为跨论文强默认；建议基准线宽约 `0.8 pt`。
2. **柔和的四组三级色板**在两篇论文中完全复现，并已通过合成图测试，优先级高于任意临时选择的 Matplotlib 默认色。
3. **色阶与透明度继续分工**：Figure 2 再次证明，类别/尺寸层级优先使用固定 RGB 浅中深色阶；alpha 留给区域、重叠与定位辅助线。
4. 新增 **zoomed inset 组件规则**：ROI、连接线、独立刻度、遮挡检测缺一不可。
5. 新增 **非对称紧凑布局规则**：按信息量分配列宽，减少重复 tick labels，并优先把少量摘要放进 panel 内部。
6. 字体尚未形成跨论文一致结论；本篇仅支持“干净的 sans-serif + 有节制的粗体层级”，暂不锁定 Helvetica 为 Skill 默认字体。

## Forward Test 02 — 合成曲线的局部放大图（用户通过）

- 测试日期：2026-07-14
- 渲染脚本：`scripts/render_local_zoom_test.py`
- PNG：`output/skill-test/04-local-zoom-inset.png`
- 矢量 PDF：`output/pdf/04-local-zoom-inset.pdf`
- 数据来源：四条确定性指数衰减曲线及轻微周期扰动，全部由脚本生成；不读取或复用 reference paper 的图像与数据。

### 本次测试的规则实现

1. 主图与 inset 均使用四边闭合画框，spine 为 `0.8 pt`；Grid 为 `#D3D3D3`、`0.5 pt`。
2. 主图显示完整的早期快速下降过程；`x=620–900`、`y=2.25–3.42` 的后期拥挤区域被 ROI 矩形标出，并在 inset 中放大。
3. inset 占主坐标区宽、高各约 `39%`，放在右侧数据稀疏区、legend 下方，不遮挡早期高值曲线或 legend。
4. ROI 与两条连接线使用 `1.0 pt`、`alpha=0.5`，比坐标框略粗但更淡；连接线从 inset 下方两角出发，不穿过 inset 内的数据。
5. inset 独立使用三个 x ticks 和三个 y ticks，并缩小 tick label 和 marker，避免照搬主图的刻度密度。
6. 颜色复用当前橙、绿、红、蓝深色色板；四条曲线另配圆、方、三角、菱形 marker，使其不只依赖颜色区分。Proposed 曲线和 legend 文字作选择性强调。

### 技术核验

- PDF 已重新渲染为 PNG 进行视觉检查：未发现裁切、文字重叠、legend/inset 冲突或连接线穿过 inset 的问题。
- `pdfimages -list` 无图像对象；最终 PDF 是重新绘制的矢量曲线、marker 和文字，没有嵌入参考论文图片。
- DejaVu Sans 与 DejaVu Sans Bold 均嵌入 PDF，保证跨环境显示稳定。

### 用户评价与规则升级

- 用户认为本次局部放大测试效果不错，并确认 Paper 02 的学习阶段可以完成。
- B03 的“ROI 小框 + 两条低透明度连接线 + 独立稀疏刻度 + 遮挡感知摆放”从论文观察升级为已通过正向测试的可执行组件规则。
- `39%` 是本次成功样例和 Figure 9 的相近起点，不固化为绝对尺寸。Agent 仍须根据 ROI 细节、legend 位置和主图空区在约 `30%–45%` 的候选范围内进行视觉校正。

## Paper 03 — CubeComposer: Spatio-Temporal Autoregressive 4K 360° Video Generation from Perspective Video

- arXiv：2603.04291v1
- 源文件目录：`reference papers/cubecomposer-spatio-temporal-autoregressive-4k-360-video-generation/`
- 归档处理：原 `arXiv-2603.04291v1.tar.gz` 已通过 gzip 与 tar 完整性检查、成功解压并删除。
- 源码清单：19 个文件，其中 `figures/` 下有 7 个可正常读取的 PDF。
- 分析状态：源文件与 Figure 映射已准备完成；等待用户指出喜欢的 pipeline 图和具体审美原因，暂不增加 pipeline 审美规则。

### Figure 与源文件映射

| 论文对象 | 源文件 | 类型与内容 |
|---|---|---|
| Figure 1 | `figures/TeaserV2.pdf` | 生成结果 teaser / demonstration |
| Figure 2 | `figures/WorkflowComparison.pdf` | 既有方法与 CubeComposer 总体 workflow 对比 |
| Figure 3 | `figures/ModelDesign.pdf` | CubeComposer 完整 pipeline overview |
| Figure 4 | `figures/ContextMechanism.pdf` | context mechanism 局部流程与 token 组成 |
| Figure 5 | `figures/CubePositionalEncoding.pdf` | continuity-aware module/design |
| Figure 6 | `figures/ComparisonV2.pdf` | 定性结果对比 / demonstration |
| Figure 7 | `figures/Ablation-Continuity.pdf` | continuity-aware 设计的定性消融 |

### 本轮 Pipeline 学习候选范围

- Figure 2：适合分析“对比式 workflow”如何在有限空间内并列旧方法与新方法。
- Figure 3：适合分析完整 pipeline 的模块分区、中间结果、主阅读路径和箭头组织。
- Figure 4：适合分析复杂上下文来源如何分组、汇合并映射到一个具体生成步骤。
- Figure 5：适合分析较小 module 或局部机制如何单独展开解释。

以上只是内容分类与文件定位，不代表已经形成审美判断。后续规则以用户明确指出的美观点为起点，再结合 PDF 矢量参数和版面测量进行核验。

### 用户明确偏好：Figure 3

1. 字体好看；边框、字体和箭头的颜色与格式协调。
2. 不同 module 使用圆角矩形包裹；虚线与实线承担不同视觉角色，部分圆角矩形带有精致阴影。
3. 整体 layout 紧凑，module 之间没有过多无效留白。Figure 3 恰好形成完整大矩形，但用户随后明确修正：可迁移规则不是“所有 pipeline 必须为矩形”，而是避免奇怪凸起和大片死空白。
4. 关键中间结果可以选择性做成圆角图片卡片，并根据图像明暗自适应边框和 caption 颜色；圆角、边框和阴影不应机械应用到高度重复的输入源图片。

### 技术证据与候选 Pipeline 规则

#### C01 — 使用人文主义无衬线字体建立温和但专业的层级

- **技术证据**：Figure 3 PDF 由 OmniGraffle 7.22.5 创建。主要字体为 `Optima-Bold`，同时使用 `Optima-Regular`、`Optima-Italic`、`Optima-BoldItalic` 和 `Optima-ExtraBlack`；Times 主要承担少量数学下标/变量，PingFang/LucidaGrande 只用于个别符号。
- **字号证据**：在原始 `1070 × 341 pt` 画布中，常用标签约 `10–12 pt`，大标题约 `11.3–13.3 pt`，细小 legend 约 `5.3–8 pt`。该 PDF 在 LaTeX 中会缩放到双栏正文宽度，因此这些绝对字号不能直接复制到其他画布。
- **候选规则**：Pipeline 图优先使用 Optima 一类的 humanist sans-serif：字形比几何无衬线更柔和，又比衬线体更适合密集模块。建立 `Bold/ExtraBlack` 主标题、`Bold` module 名、`Italic` 过程说明、`Regular` legend 的四级层级；不要让所有文字都使用同一粗细。
- **可移植性**：Optima 是明确的审美参考，但不是所有 Linux 环境都具备。最终 Skill 应先检查字体；缺失时选择形态接近且可嵌入的 humanist sans-serif，而不是静默回退到任意默认字体。
- **证据强度**：1/1，用户明确喜欢；等待后续 pipeline 论文验证字体类型。

#### C02 — 让文字、边框和箭头共享同一套语义色

Figure 3 的关键颜色不是装饰性色板，而是贯穿标题、容器和箭头的语义系统：

| 角色 | Hex | 实际用途 |
|---|---:|---|
| 时间维度深红 | `#B1001C` | Temporal Dimension、time-window 标题、外层时间框和时间箭头 |
| 空间维度深蓝 | `#003776` | Spatial Dimension、Face 标题、face 容器和空间箭头 |
| Attention 深紫文字 | `#310067` | Sparse Context Attention 标题与强调文字 |
| Attention 淡紫边框 | `#907CBB` | SCA 标签框、右侧说明 panel 与虚线 callout |
| 主信息黑 | `#000000` | 核心模型名、主数据流、输入输出标题 |
| 次级深灰 | `#666666` | Context、Update、覆盖率和辅助说明 |
| 中性边框灰 | `#A5A5A5` | 实体卡片边框、辅助更新箭头 |
| 浅分隔灰 | `#D9D9D9` | 次级分隔线与弱结构 |
| 卡片底色 | `#FFFFFF` | 绝大多数模块和容器背景 |

- **候选规则**：先为 pipeline 中的语义维度分配颜色，再把同一颜色同步用于该维度的标题、边框和方向箭头。不要出现“标题一种颜色、边框另一种无关颜色、箭头再随机一种颜色”的割裂。
- **用色限额**：复杂 pipeline 的强语义色控制在约 3 组；其余主流程使用黑、白、灰。Figure 3 的三组分别是时间红、空间蓝和 attention 紫。
- **证据强度**：1/1，暂定 pipeline 色彩语法。

#### C03 — 圆角矩形保持统一，虚实线表达不同层级

- **技术证据**：主要外层 time window、内层 face panel、planning slot、输入容器、模型条和 attention panel 都使用圆角路径；常见圆角半径约 `6 pt`。主要逻辑分组边框为 `1 pt`，虚线模式统一为 `2 pt on / 2 pt off`，并使用 round cap/round join。
- **层级事实**：
  - 红色虚线圆角框：时间窗口、规划前后等 temporal/repeated scope；
  - 蓝色虚线圆角框：face、空间单元和 generation slot；
  - 灰色实线圆角框：输入、latent、context、生成结果和模型等具体实体；
  - 紫色实线圆角框：需要重点解释的自定义 attention module/callout。
- **候选规则**：使用同一种圆角几何建立家族感，再用线型和颜色区分语义。默认把**虚线框**用于范围、重复单元、时间窗口、可迭代区域或 placeholder group；把**实线框**用于具体 module、数据对象、结果卡片和重点 callout。
- **防误用**：不要为了“丰富”而随机混用虚实线；同一线型必须在整图中保持同一含义。必要时在 legend 中解释。
- **证据强度**：1/1，用户明确偏好。

#### C04 — 箭头的颜色、粗细和方向分别承担语义

- **技术证据**：时间与空间的横向方向箭头分别使用 `#B1001C` 和 `#003776`、约 `2 pt` 实线及同色实心三角箭头；核心数据流使用约 `1 pt` 黑色实线箭头；`Update` 使用约 `2 pt` 的 `#A5A5A5` 斜向箭头；SCA callout 使用 `#907CBB`、约 `1 pt`、`2/2` 虚线连接。
- **候选规则**：
  - 黑色实线箭头表示主数据流；
  - 同色粗横箭头表示维度、顺序或阅读方向；
  - 灰色斜箭头表示更新、回写或次级变换；
  - 紫色等语义色虚线表示 callout、对应关系或非主流程连接。
- **布局约束**：优先使用水平/垂直主路径；斜线只用于明确的 update 或跨层关系。保持箭头头部形状统一，减少交叉和无意义折线。
- **证据强度**：1/1，暂定箭头语法。

#### C05 — 阴影只赋予“实体卡片”，逻辑分组保持扁平

- **技术证据**：PDF 使用大量 mask-based soft shadow。阴影主要出现在输入/规划大卡片、长条 Transformer module、latent/context 小卡片、generated/final output 图像以及右侧 SCA panel；红蓝虚线的时间/空间逻辑分组大多保持无阴影、白底扁平。
- **候选规则**：用阴影区分“可以被拿起来的具体实体/前景卡片”和“只负责划定范围的抽象 group”。不要给每一层嵌套框都加阴影，否则紧凑图会变脏、层级会反转。
- **实现起点**：若重建草版，可从低透明度中性灰、约 `1.5–3 pt` 偏移和 `2–4 pt` 柔化开始，再按最终缩放尺寸检查。这个范围是复现视觉效果的建议值，不是从压缩 PDF 中精确恢复的原始 OmniGraffle 参数。
- **证据强度**：1/1，用户明确喜欢选择性阴影。

#### C06 — 先确定目标版面，再控制外轮廓与无效留白

- **画布证据**：Figure 3 页面为 `1070 × 341 pt`，宽高比约 `3.14:1`。主要内容从约 `x=6` 延伸到 `x=1064`，使用约 `98.9%` 的页面宽度；主容器大致共享 `y≈25–330` 的上下边界。
- **宏观分区**：左侧约 `27%` 宽度放输入、条件构建和 generation-order planning；中间约 `58%` 放多个时间窗口和 face generation；右侧约 `14%` 放 SCA 机制说明与 legend。比例是本图事实，不应写死为所有 pipeline 的固定模板。
- **对齐证据**：相邻主时间窗口之间只有约 `9–10 pt` 间隔。右侧 SCA panel 几乎贴齐主流程边缘。多个大分区顶部、底部和外边界对齐，因此局部内容虽复杂，整体仍形成一个稳定的大矩形。
- **结构黏合剂**：中间的长条 `Spatio-Temporal Auto-regressive Video Diffusion Transformer` 横跨多个 face panel，像一条水平腰带把重复的小模块连接成同一个系统；它同时减少了为每个 face 重复绘制完整模型的空间浪费。
- **用户修正**：Figure 3 的矩形外形是一个成功实例，不是所有 pipeline 的强制形状。真正需要迁移的是紧凑 layout：图形应高效占用目标单栏/双栏画布，不能因为某一处异常向上、向下或向侧面凸出，迫使整张图扩大并留下大片空白。
- **候选规则**：
  1. 先确定最终单栏、双栏或横跨页面的目标宽高比，再规划 2–4 个宏观分区；
  2. 让主要 module 的边缘尽量对齐，保持稳定、重复的 gutter，减少随机参差；
  3. 将 callout、legend、局部机制和支路优先嵌入已有空区，或与相邻模块重新排成一行/一列；
  4. 如果一个必要模块明显凸出，应重新平衡其他模块、改变流向或调整分区，而不是接受由凸出部分制造的大面积死空白；
  5. 允许 L 形、分叉形、上下双流等非矩形结构，只要它们符合算法叙事并且整体空白受控、阅读路径清楚。
- **紧凑性检查**：在草版和最终尺寸各检查一次内容 bounding box、四周空白、模块间 gap，以及由局部突起包围出的空洞。矩形度本身不是评分项；无效留白、突兀轮廓和低空间利用率才是问题。
- **证据强度**：用户明确规则；Figure 3 为 1 个高空间利用率实例。

#### C07 — 从 Figure 3 抽象出的首轮草图模板

当用户只有算法叙事、尚未准备完整中间结果时，可把 Figure 3 的布局语法迁移为以下**低保真模板**，但不能复制其算法内容：

1. 左区：`[请提供：输入示例] → [待确认：预处理/条件构建] → [待确认：顺序或规划结果]`；
2. 中区：用多个虚线 scope 表示阶段/时间窗口，在内部放 `[数据/latent]`、`[context]`、`[请提供：中间结果]`；
3. 使用一条贯穿式公共模型/module 横条连接重复阶段，避免重复画相同网络；
4. 右区：放 `[请提供：最终输出]`，并为最重要的创新 module 预留一个局部 callout/legend；
5. 先让已知内容紧凑填充目标画布，并把 placeholder 安排在不会制造大片死空白的位置，再请用户补充真实中间结果、模块名称、分支和训练/推理差异。

这是一种用于解除“空白页困境”的版式起点，不是固定的矩形模板或默认终稿，也不允许 Agent 根据占位符虚构算法内容。

#### C08 — 关键中间结果使用对比度自适应的图片卡片

- **技术证据**：Figure 3 中的 `Noisy Latents`、三张 `Generated Video` 和 `Final Output` 都是圆角图片。深色/复杂图像外使用约 `1 pt` 的白色 `#FFFFFF` 边框；偏亮的 `Context` 卡片使用约 `1 pt` 的中性灰 `#A5A5A5` 边框。常见圆角仍约为 `6 pt`，并配合选择性 soft shadow。
- **候选规则**：对关键中间结果、阶段性输出或需要读者停留观察的图像，按以下顺序设计：
  1. 将图片裁切到与同级卡片一致的比例；
  2. 仅在它承担“主要结果卡片”角色时使用圆角；
  3. 检查图片**边缘区域**而不只是整张图的平均明暗，因为边框实际与边缘像素相邻；
  4. 边缘偏暗时使用白色/近白边框，边缘偏亮时使用深灰/语义深色边框；
  5. 在最终论文缩放尺寸检查边框是否仍然可见，再决定是否加低透明度阴影。
- **线宽建议**：Figure 3 源 PDF 的图片框约为 `1 pt`。Skill 不应把源值写死；应以最终显示尺寸为准，从约 `0.8–1.2 pt` 的可见边框起步，避免因整体缩放变成几乎不可见的细线。
- **混合边缘处理**：如果图片四周同时包含极亮和极暗区域，单色边框可能局部消失。可使用近白内描边 + 很淡的深色外阴影，或深色内描边 + 浅色底托；不要直接加很粗的高对比外框。
- **证据强度**：1/1，用户明确偏好并有 Figure 3 实例支持。

#### C09 — 图片内 caption 根据局部背景而不是全图明暗选择颜色

- **技术证据**：`Noisy Latents` 与 `Generated Video` 的图内文字使用白色 `#FFFFFF`、Optima Bold；浅色 `Context` 卡使用 `#666666`。常用 caption 在原始资产中约 `10 pt`，通常控制为 1–2 行并居中，没有使用大块不透明 banner。
- **候选规则**：
  1. 先寻找图中低显著性、纹理较少且不会遮挡关键内容的区域；
  2. 在该**文字落点的局部背景**上判断明暗：暗底用白/近白文字，亮底用深灰/近黑文字；
  3. Caption 尽量短，通常不超过两行；字号只需建立可读层级，不应占据主要画面；
  4. 背景明暗变化剧烈时，可增加非常轻的文字阴影、细描边或小范围半透明底托；底托不得覆盖大片结果；
  5. 如果找不到不遮挡内容且对比稳定的位置，把 caption 移到图片下方或卡片外部，不强行叠字。
- **防误用**：不要因为整张图片“总体偏暗”就默认白字；文字所在位置可能恰好是高亮区域。颜色判断应针对实际 caption 区域。
- **证据强度**：1/1，用户明确偏好。

#### C10 — 圆角、边框和阴影是重点标记，不是所有图片的默认滤镜

- **技术证据**：Figure 3 的主要 generated/intermediate result 使用圆角、白边和阴影；左侧高度重复的 perspective input 拼图、masked views 与 cubemap face strip 则主要保持方形切片或紧凑堆叠，没有把每一张都做成独立浮动卡片。
- **候选规则**：
  - 主要中间结果、代表性阶段输出、最终输出：可使用圆角 + 对比边框 + 轻阴影；
  - 高度重复的输入帧、source views、token/patch 阵列和小型缩略图：优先保持方形、共用外容器或紧凑堆叠；
  - 同一组中只突出少量真正需要读者观察的图片，避免几十个圆角阴影卡片同时竞争注意力。
- **草版占位符**：首次 pipeline wireframe 应标注哪些位置建议放“主要结果卡片”，哪些位置只需“重复输入缩略图阵列”，并请用户分别提供对应素材；不要在素材缺失时假定每个 placeholder 都采用同一种图片效果。
- **证据强度**：1/1，用户明确说明这是可选设计而非全局要求。

## 论文 4：ToonComposer

### 来源登记

- **标题**：*ToonComposer: Streamlining Cartoon Production with Generative Post-Keyframing*
- **arXiv 源文件**：`2508.10881v1`
- **本地目录**：`reference papers/tooncomposer-streamlining-cartoon-production-with-generative-post-keyframing`
- **处理状态**：已验证并解压 LaTeX 源文件；原始 `tar.gz` 已删除。
- **当前阶段**：仅完成资料登记和视觉预览，等待用户逐图指出审美重点；尚未把本论文的视觉特征提升为新规则。

### Figure 对照

1. Figure 1 — `figures/TeaserV3.pdf`：输入关键帧/草图与生成视频结果展示。
2. Figure 2 — `figures/Workflow-CmpV2.pdf`：传统工作流、既有 AI 工作流与 ToonComposer 工作流对比。
3. Figure 3 — `figures/Method.pdf`：ToonComposer 总体模型 pipeline。
4. Figure 4 — `figures/SLRA.pdf`：Spatial Low-Rank Adapter 局部模块结构。
5. Figure 5 — `figures/SketchSamples.pdf`：训练与评测所用 sketch 类型。
6. Figure 6 — `figures/Comparison-Synthetic.pdf`：synthetic benchmark 定性对比。
7. Figure 7 — `figures/Comparison-Real.pdf`：PKBench 真实手绘草图定性对比。
8. Figure 8 — `figures/Ablation-SLRA.pdf`：SLRA 定性消融。
9. Figure 9 — `figures/Usecase-RegionWise.pdf`：region-wise control 案例。
10. Figure 10 — `figures/MultiFrameControl.pdf`：不同数量关键帧的控制效果。

### 待用户确认的观察

- 不因为作者与论文 3 相同或风格相近而自动复制结论。
- 用户明确认可的设计点将先记录为本论文证据，再判断它是强化 C01–C10、修正规则，还是形成新的 pipeline 规则。

### Figure 2 — 单栏 workflow 对比图

#### 用户明确认可的设计点

1. 单栏画布中的整体布局紧凑，外侧 bounding box 内没有大面积无效空白；矩形外轮廓只是本图结果，不是所有 pipeline 的硬性要求。
2. 大 workflow group 使用灰色与橙色的圆角矩形背景，并采用克制的渐变；渐变是可选手段，关键是低饱和、大面积底色与深色语义色的高级搭配。
3. 外层 group、内部关键 sub-module 和 group caption 形成颜色呼应，例如 `Previous Workflow` 使用对应灰色，`Our Workflow` 与 `ToonComposer` 使用同一橙色。
4. 箭头、字体、黑白灰关系和整体细节精致；连接线的视觉层级需要与模块层级一起设计。

#### D01 — 用“死空白审计”约束紧凑度，而不是强制矩形轮廓

- **技术证据**：Figure 2 源 PDF 为 `404 × 155 pt`，宽高比约 `2.61:1`，并在 LaTeX 中按单栏 `\linewidth` 放置。240 dpi 渲染画布为 `1347 × 517 px`，以接近白色为背景裁切后，实际内容 bounding box 约为 `1340 × 506 px`，占画布宽度约 `99.5%`、高度约 `97.9%`。
- **布局证据**：上方 previous workflow 与下方 our workflow 共用左侧输入区域和右侧输出 filmstrip；上下两条路径没有重复绘制同一组锚点。两块大背景上下紧邻、左右边缘对齐，输出 filmstrip 同时覆盖两行高度，从而填补右侧空间并加强对比关系。
- **候选规则**：草图完成后，显示整个内容 bounding box，并检查内部是否存在面积接近一个主要 module、却不承载分组、路径、caption 或视觉呼吸功能的连续空区。若存在，应优先通过共享输入/输出锚点、移动 callout、调整流向、重新分配 module 尺寸或合并重复内容来压缩。
- **防误用**：不要用简单的“像素填满率”追求密度；模块内部 padding、组间 gutter 和阅读路径需要保留。真正应消除的是由突兀分支、错位边缘和重复绘制制造的死空白。
- **证据关系**：强化并细化 C06；新增“共享锚点压缩对比 pipeline”的具体做法。

#### D02 — 大分组使用浅渐变，深色只作为语义锚点

- **技术证据**：上方灰色 workflow 背景为从白色 `#FFFFFF` 到中性灰 `#A5A5A5` 的轻微斜向渐变，方向约为 `-10°`；下方橙色 workflow 背景为从白色到浅鲑橙 `#F3BAB1` 的斜向渐变，方向约为 `+23°`。两者都是低对比、低饱和的大面积底色。
- **前景色**：灰色语义文字为 `#666666`；橙色语义文字为深焦橙 `#B34400`；主流程与普通 module 文字为 `#000000`，卡片与反白文字为 `#FFFFFF`。
- **候选规则**：为一个 workflow group 选择一组“浅背景 + 深锚点色”。浅背景承担区域分组，深色只用于 group caption、该组最有辨识度的 module 名或少量强调。不要让大背景直接使用高饱和橙色，也不要把所有内部文字都染成锚点色。
- **渐变约束**：渐变不是默认要求。仅当它能柔化大色块、暗示阅读方向或区分并列区域时使用；端点颜色应相近、变化平缓，并在最终缩放和灰度打印下检查。纯色若更清楚，应优先纯色。
- **证据强度**：1/1，用户明确认可 Figure 2 的灰橙搭配与渐变。

#### D03 — 外层背景、前景卡片和素材采用三种不同的视觉重量

- **技术证据**：previous/our workflow 使用无明显描边的浅色圆角背景；`Keyframing`、`Inbetweening Model`、`Colorization Model` 和 `ToonComposer` 等前景实体使用白色圆角卡片与 soft shadow；sketch、reference frame、per-frame sketch stack 和 output filmstrip 则保留为具体图像素材或薄线框阵列。
- **候选规则**：
  1. 用浅色大圆角背景表示 workflow scope；
  2. 用白色圆角 + 轻阴影表示可操作的 model/stage 实体；
  3. 用实际图片、缩略图栈或简洁薄框表示输入、条件和输出数据。
- **作用**：读者无需依赖额外 legend，就能从视觉重量判断“这是区域”“这是模块”还是“这是数据”。阴影继续遵守 C05：只赋予前景实体，不给每层 scope 都加阴影。
- **证据强度**：1/1，Figure 2 实例强化 C03 与 C05。

#### D04 — 颜色呼应只落在关键标签上，不机械覆盖所有子模块

- **技术证据**：`Previous Workflow` 与 `(By Human Artists)` 使用 `#666666`；`Our Workflow`、`ToonComposer` 和 `(Generative Post-keyframing)` 使用 `#B34400`。相比之下，`Sparse Keyframe Sketches`、`Inbetweening Model`、`Per-frame Sketches` 和 `Colorization Model` 等通用流程文字仍使用黑色。
- **候选规则**：让 group caption、该组独有/创新的 sub-module 标题以及必要的局部强调共享同一个深锚点色；让通用处理步骤保持黑色或中性色。这样既形成内外呼应，也能把注意力集中到方法差异上。
- **防误用**：不要把“子模块颜色呼应”解释为所有子模块文字必须与外框同色。颜色应表达归属和创新重点，而不是简单装饰。
- **证据强度**：1/1，用户明确认可，技术取样进一步限定了应用范围。

#### D05 — 主数据流与辅助结构线分层，箭头不必全部彩色

- **技术证据**：Figure 2 的主要方向箭头实际统一使用约 `1 pt` 黑色实线与黑色三角箭头；灰色 `#A5A5A5` 用在输入 scope 的 `1 pt`、`2/2` 虚线边框，以及 sketch stack 的约 `0.5 pt` 薄线框。也就是说，本图主要通过黑色数据流与灰色辅助结构线形成层级，而非为每条箭头分配不同颜色。
- **候选规则**：默认让主数据流保持黑色或最深中性色，使路径稳定清楚；让边界、堆叠轮廓、对应关系等辅助线变浅或使用虚线。只有当图中确实存在多种需要读者区分的关系时，才按语义为箭头上色，并与 module/group 的锚点色保持一致。
- **字体证据**：PDF 仅嵌入 `Optima-Bold`；常用源字号约 `8–10 pt`。字体和粗细高度统一，层级主要通过字号、颜色、位置和卡片重量建立，继续强化 C01 的 humanist sans-serif 方向。
- **证据关系**：保留用户对“箭头需要区分”的审美目标，同时根据源 PDF 把本图的实际实现准确记录为线色、线型和视觉重量的区分。

### Figure 3 — ToonComposer 总体 pipeline

#### 用户明确认可的设计点

1. 双栏长条画布中的内容紧凑，bounding box 内没有明显无效留白；长矩形外形是本图结果，不是所有 pipeline 的强制模板。
2. 主要阅读方向清楚地从左向右展开，符合输入→处理→输出的视觉习惯。
3. 字体与配色精致；文字颜色根据所在局部背景选择，亮底使用暗字、暗底或彩色实体使用白字，同一 scope 下的 caption 保持统一。
4. 箭头具有颜色层级，转角圆润；大量圆角边框、轻微着色和选择性阴影共同提升精致度。

#### D06 — 以水平主脊柱组织双栏长图，把支路收进同一高度包络

- **技术证据**：Figure 3 源 PDF 为 `641 × 124 pt`，宽高比约 `5.17:1`，在 LaTeX 中使用 `figure*` 与双栏 `\linewidth`。240 dpi 渲染为 `2137 × 414 px`，内容裁切 bounding box 约为 `2129 × 406 px`，占画布宽度约 `99.6%`、高度约 `98.1%`。
- **结构证据**：输入图像栈、VAE encoder、projection、sparse sketch injection、Diffusion Transformer、projection/unpatchify、VAE decoder 和输出视频栈沿一条左→右主脊柱排列。`Position-aware Residual` 被收在中心容器上部，`Position Encoding Mapping` 被收在下部，SLRA 被嵌入 transformer 下半区；legend 则利用输出阶段下方的剩余空间，没有额外增加整行。
- **候选规则**：为双栏横向 pipeline 先建立一条贯穿输入与输出的水平主脊柱。conditioning、residual、mapping、adapter、loss 或 callout 优先放在主脊柱上下的已有空间，并尽量不突破整图的上下高度包络；把 legend 放入结构自然留下的空区。
- **防误用**：紧凑不等于把所有内容挤到一起。主路径、局部回路和文字仍需保留稳定 gutter；应消除的是由支路外凸、重复模块和孤立 legend 制造的大片死空白。
- **证据关系**：强化 C06 与 D01，并新增“水平主脊柱 + 上下嵌入支路”的具体双栏模板。

#### D07 — 默认左→右叙事，把例外路径限制为局部回路

- **技术证据**：输入位于最左，输出位于最右；绝大多数主箭头水平向右。中心虽然存在 position-aware residual 的回指与 position encoding 的上送路径，但它们都被限制在 `Sparse Sketch Injection` scope 内，没有改变整图的主阅读方向。
- **候选规则**：当算法天然是输入→处理→输出时，首选左→右。让主要阶段标题、模块中心和主箭头共享近似水平基线；skip、feedback 和 conditioning 通过短的上绕/下绕局部回路表达，完成后立即回到主脊柱。
- **转向条件**：如果算法本质是层级树、循环优化、上下双流或 encoder–decoder 对称结构，可以选其他方向；但仍需选定唯一的主阅读顺序，避免读者在多个方向之间反复猜测。
- **证据强度**：1/1，用户明确认可。

#### D08 — 文字颜色按局部背景分配，并与语义色共同建立层级

- **技术证据**：
  - 深色输入图、reference frame、深蓝 `Video Tokens`、灰色 `Sketch Tokens` 和红色 `SLRA` 上使用白色 `#FFFFFF` 文字；
  - 白色或浅灰 module 上主要使用 `#666666` 或 `#000000`，例如 Diffusion Transformer、DiT Block、projection 与 decoder；
  - 淡色 scope caption `Sparse Sketch Injection`、`Cartoon Adaptation` 使用统一的浅灰 `#A5A5A5` 与 Bold Italic；
  - latent、部分 input label 和 `Frozen` 使用深蓝 `#003776`；`Trainable` 使用深红 `#B1001C`。
- **字体证据**：主要字体为 `Optima-Bold`、`Optima-BoldItalic` 和 `Optima-Regular`，数学符号使用 Latin Modern Math。它再次支持 humanist sans-serif + 有限 italic 层级，不是所有文字统一一种 weight/style。
- **候选规则**：先确定文字落点，再检查该局部区域的最亮与最暗部分。亮底选黑/深灰/语义深色，暗底或饱和彩底选白色；渐变底必须按文字覆盖范围中的最低对比度判断，不能只看整张卡片的平均明暗。
- **处理顺序**：优先换文字颜色，其次移动到更稳定的局部背景；仍不足时才增加很轻的描边、阴影或小范围半透明底托。不要用大块不透明标签遮住 module 或中间结果。
- **证据关系**：把 C09 的“图片 caption 局部对比”升级为适用于所有 module、token、legend 和 scope caption 的通用规则。

#### D09 — 用圆角、线型、渐变和阴影共同编码层级

- **技术证据**：
  - `Sparse Sketch Injection` 外层 scope 使用 `#A5A5A5`、约 `0.5 pt`、`2/2` 虚线圆角框，圆角约 `7 pt`；
  - `Cartoon Adaptation` 内层 scope 使用相同灰色虚线语法，圆角约 `4 pt`；
  - 具体 module、projection、position mapping、token、DiT block、SLRA 和 legend 使用约 `4–7 pt` 的圆角或圆滑异形卡片；
  - 多个前景实体带 mask-based soft shadow，而抽象虚线 scope 基本保持扁平。
- **候选规则**：让抽象 group 使用浅色虚线圆角边界，让具体可操作 module 使用实线/白边、浅色或渐变填充与轻阴影；重复的小模块共享相同圆角、填充和阴影参数，建立家族感。
- **防误用**：圆角、渐变和阴影必须有层级意义。不要给每层嵌套 scope 都加阴影，也不要让所有卡片使用不同渐变；最终尺寸下若阴影只形成脏边，应降低透明度、缩小偏移或直接取消。
- **证据关系**：进一步强化 C03、C05 与 D03。

#### D10 — 灰色承担主连接，深蓝只强调特殊条件流，转角统一圆润

- **技术证据**：多数主连接使用 `#666666`、约 `0.5 pt` 的实线与小型实心三角箭头；进入 transformer 的特殊 token/condition 连接和 timestep 连接使用 `#003776`。连接线统一使用 round cap/round join，直角转弯通常通过约 `3 pt` 的圆弧/Bezier 过渡，而不是尖锐的 90° 折角。scope 边界则使用 `#A5A5A5`、约 `0.5 pt`、`2/2` 虚线。
- **候选规则**：默认用中性深灰保持主数据流稳定；只为确实需要单独识别的 conditioning、time、trainable/frozen 或其他语义连接使用锚点色。所有同类折线路径采用统一圆角半径、线宽和箭头头部。
- **路由规则**：优先水平/垂直段，转角圆滑；避开文字和卡片阴影；局部反馈线从模块边缘出发并尽快回到目标，不让大弧线穿越整张图。
- **技术校正**：本图实际没有用红色箭头表达 trainable；红色主要出现在 SLRA、火焰图标和 legend。Skill 应学习“颜色按语义分配”，不能把图中出现过的每个强调色都自动用于箭头。
- **证据强度**：1/1，用户明确认可箭头分层与圆润转角。

#### D11 — P4 的四组卡片渐变与文字搭配

| 实体角色 | 渐变端点 | 推荐文字 |
|---|---:|---:|
| Video token / 深蓝实体 | `#92BFFF ↔ #0C2734` | `#FFFFFF` |
| Sketch token / 灰色实体 | `#939595 ↔ #DADADA` | `#FFFFFF`，需检查最浅端对比 |
| DiT block / 中性 module | `#FFFFFF ↔ #DADADA` | `#666666` 或更深 |
| SLRA / trainable module | `#901113 ↔ #DFBCB7` | `#FFFFFF`，需检查最浅端对比 |

- **候选规则**：渐变端点、文字和语义锚点应作为一组选择。若白字在渐变浅端不够清楚，应调整渐变方向、缩小文字覆盖范围或加深浅端，而不是机械保持源值。
- **全局更新**：以上颜色已并入全局 P4，不限制为 pipeline 专用色；统计图、表格、timeline 或其他图型若具有相同语义与面积关系，也可以选用。
- **证据强度**：1/1，Figure 3 同图验证；等待后续作品验证跨图型迁移。

## Forward Test 03 — AsyncEvGS pipeline 草图（V2 获得初步认可）

- **测试论文**：*AsyncEvGS: Asynchronous Event-Assisted Gaussian Splatting for Handheld Motion-Blurred Scenes*。
- **输入文件**：`Pipeline-test-paper.pdf`。
- **防视觉泄漏**：本轮只使用 `pdftotext` 阅读论文正文、方法与补充材料，没有渲染或查看论文原 Figure；草图不能依赖原作者的 pipeline layout。
- **草图状态**：明确标记为 `DRAFT · CONCEPT`，使用真实论文模块名与损失项；缺少的 RGB、event、结构图、confidence map 和最终结果均保留为 placeholder。
- **草图文件**：`.codex/visualizations/2026/07/14/019f616c-9eb5-7c10-8da4-8fc8755fc055/asyncevgs-pipeline-draft.html`。

### 从正文提取的 pipeline 事实

1. 异步双相机输入：1280×720 motion-blurred RGB frames 与 1280×720 raw event streams，不要求硬件时间同步。
2. Event bridge：raw events 经 E2VID 得到 grayscale frames，再进行 bilateral denoising 与 multi-frame brightness equalization。
3. Cross-domain initialization：blurred RGB 与预处理 event-derived frames 一同输入 VGGT，得到所有 RGB/event view poses 与 dense point cloud；点云以 50% confidence threshold 过滤，poses 在后续 3DGS 优化中联合 refine。
4. Stage 1：从 VGGT 初始化训练 RGB-only coarse 3DGS `G_ref`，10k iterations，使用 `L_blur`；随后复制并冻结为 color reference。
5. Stage 2：从同一 VGGT 初始化训练新的 RGB+Event 3DGS，30k iterations，并联合优化 poses。
6. 五个 loss：RGB/deblur 的 `L_blur`、`L_reg-r`；event-guided 的 `L_evs`、`L_struct`；跨阶段 color distillation 的 `L_reg-e`。
7. `L_struct`：比较 event-view rendering 与 E2VID target 的 structure maps，使用 multi-scale confidence `W` 加权 SSIM，并移除 luminance term。
8. 输出：兼具 sharp high-frequency structure 与 faithful RGB color 的 optimized 3DGS / novel views。

### 本轮主动应用的审美规则

- 左→右主阅读方向，RGB 与 event 两条语义流在 VGGT 汇合；
- 使用 P4 深红/深蓝/紫色组合，灰色承担主结构；
- 大 scope 使用圆角虚线且保持扁平，前景 module 使用圆角与选择性 soft shadow；
- 深色 E2VID、weighted SSIM 与 output module 使用白字，浅色卡片使用深色字；
- 主流程使用实线，loss/teacher 使用虚线，并使用圆润转角；
- event structure novelty 被嵌入中心下方空间，Stage 1 被嵌入 Stage 2 上方，避免额外扩张 bounding box；
- 在桌面宽度显示完整 pipeline，在窄宽度切换为纵向结构摘要。

### 等待验证的问题

- 用户是否认为整体紧凑度、信息层级、配色、字体、箭头与圆角/阴影符合已学习审美；
- Stage 1 与五个 loss 的信息密度是否合适，还是需要进一步简化；
- 初版是否成功告诉作者下一轮应补充哪些中间结果，而没有冒充最终 publication-ready 图。

### 用户对 V1 的评价与暴露出的失效模式

- **保留项**：整体方向正确；配色、圆角半径、曲线箭头和字体获得认可。
- **主要失败 1 — 外接框不紧凑**：最左侧一级 scope 与中间 scope 的底部没有对齐，导致最终 bounding box 内出现明显死空白。仅仅“局部卡片排列紧凑”不足以通过；还必须检查一级容器的共同上下锚点与整体轮廓。
- **主要失败 2 — 过度文字化**：V1 虽然写出了 pipeline 事实，但中间结果几乎全被文字框代替，没有为真实图片分配足够面积，因此只能说明算法，不能有效指导作者继续排版。
- **主要失败 3 — 交付不可继续编辑**：PNG 只能作为预览；若用户需要重新移动 module、替换中间结果和修改箭头，栅格图会迫使其重新临摹。pipeline 草案必须默认交付 Figma 可导入的分组 SVG，PPTX 为可选补充。
- **主要失败 4 — 阴影规则没有落实**：虽然此前已经学习“选择性阴影”，V1 的最终观感没有形成足够清楚的前景悬浮层级。规则必须从候选审美项升级为导出前的显式检查项。

### V2 修正策略

1. 将五个一级 scope 统一到同一顶部与底部锚点，固定列间 gutter；只让连接线在极小范围内越出主框。
2. 扩大 RGB、event、E2VID、geometry/poses 和最终 novel-view 的图片槽位，并为每个槽位建立独立可替换 group。
3. 对 E2VID、VGGT、Stage 1、Stage 2、关键输入卡和主要输出卡使用一致的轻阴影；逻辑 scope 继续保持扁平虚线。
4. 使用标准 SVG 元素与命名 `<g>` 图层，避免 raster flatten；将 SVG 作为主交付，PNG 作为视觉核验预览。
5. 新版文件：`output/pipeline-test/v2/pipeline-test-layout-v2.svg`。

### 用户对 V2 的评价

- 用户认为 V2 在 layout 上比 V1 好很多，作为供用户继续工作的起始模板已经达到“不错”的水平。
- 这次评价验证了共同上下锚点、紧凑 bounding box、较大图片替换区、选择性阴影和 Figma 优先分组 SVG 的修正方向。
- 本轮只将上述方向记为 pipeline 分支的稳定规则；不把 AsyncEvGS 的五栏结构、具体列宽或模块顺序固化成所有方法的通用模板。
- 测试输出已统一归档到 `output/pipeline-test/`：`v1/` 保留失败样例用于对照，`v2/` 保留当前认可版本。

## Paper 05 — Scaling View Synthesis Transformers

### 文件与 Figure 映射

- **标题**：*Scaling View Synthesis Transformers*
- **源码目录**：`reference papers/scaling-view-synthesis-transformers/`
- **Figure 5**：`images/qualitative_twoview_fixed.png`，由 `figures/qualitative_two_view.tex` 以双栏 `figure*`、`width=\textwidth` 插入。
- **图像尺寸**：`6456 × 3594 px`，带透明背景；CVPR 模板的 `\textwidth` 为 `6.875 in`，因此下述源像素线宽换算到最终双栏版面时约乘以 `495 / 6456 pt/px`。

### Figure 5 — 带结构分隔与紧凑标签的 NVS 定性比较矩阵

#### 用户明确认可的设计点

1. 所有行列紧密而工整地对齐，整体 bounding box 内没有大块无意义空白。
2. 上下两个 case 各占两行，中间使用一条实线横向分隔；Context、不同 FLOPs 的预测结果与 Ground Truth 之间使用虚线竖向分隔，功能区域清楚。
3. 每张子图都有粗细适中的黑色边框，显著提升图块的完成度和质感。
4. 顶部 `Context`、各 FLOPs 和 `Ground Truth` 共享同一文字基线，居中对应各自列；文字与图像之间的距离紧凑但不拥挤。
5. 右侧 method 标签采用斜排，使其进入窄侧栏并补足双栏宽度。斜排本身不是硬性模板，底层目标是根据剩余空间调整标签方向，保持紧凑外轮廓。

#### E01 — 分隔线必须表达明确层级，不作为装饰随机加入

- **技术证据**：Figure 5 使用三种边界语法：每张 tile 的黑色实线边框；两条贯穿结果行的黑色竖向虚线，用于隔开 `Context | scaling predictions | Ground Truth`；一条横跨主要图像区域的黑色实线，用于隔开上下两个 case。
- **源图尺寸**：tile 边框、竖向虚线和 case 横线的主线宽均约为 `12 px`，按最终 `6.875 in` 双栏宽度换算约为 `0.92 pt`。竖向虚线约为 `24 px on / 24 px off`，换算后约为 `1.84 pt on / 1.84 pt off`。
- **候选规则**：
  1. 用 tile 实线边框定义单张结果；
  2. 用贯穿多行的虚线分隔不同列族、输入/预测/真值或其他功能区域；
  3. 用贯穿多列的实线分隔不同 case、scene 或主要实验组。
- **防误用**：只有读者确实需要理解分组时才增加分隔线。线型在整图中必须保持同一语义；不要在没有层级变化的位置加入横线，也不要让 separator 穿过文字或主体图像。

#### E02 — 单图边框从约 `0.8–1.0 pt` 起步，并在最终尺寸复检

- **技术证据**：每张结果 tile 的外框约 `12 px`，而 tile 外尺寸约 `768 × 768 px`；边框约占 tile 宽度的 `1.56%`，最终双栏尺寸约为 `0.92 pt`。它足以在亮、暗两种场景中保持边界，却不会抢过图像内容。
- **候选规则**：2D/NVS 结果矩阵默认测试黑色或近黑色 `0.8–1.0 pt` 边框。背景非常暗时可改用近白边框，或为整组增加浅底托；边框选择应同时检查图像四周边缘，而不是只看平均亮度。
- **检查项**：所有 tile 的边框线宽、颜色、圆角状态必须一致；拼接后不得出现相邻边框叠加成双倍粗线。最终按论文实际宽度渲染后再判断，而不是只看高分辨率源图。
- **证据关系**：补充并验证 Q08 的“细边框模式”，同时与 pipeline 图片卡片的对比度自适应规则保持一致。

#### E03 — 普通 gutter 与语义分组 gap 使用成组倍数

- **技术证据**：同一结果区域内，相邻 `768 px` tile 的常规水平/垂直 gutter 约为 `48 px`，最终约 `3.68 pt`，恰为边框线宽的约 `4×`。Context 与第一列预测、最后一列预测与 Ground Truth 之间的功能区 gap 约为 `192 px`，即常规 gutter 的 `4×`，竖向虚线位于其中央。两个 case 之间则采用约 `48 px + 12 px separator + 48 px` 的结构。
- **候选规则**：先定义一个标准 tile gutter `g`，再让功能区 gap 使用 `2g–4g` 等清楚倍数并在其中放 separator；不要为每一处间距单独手调。Figure 5 的 `g≈3.7 pt`、group gap `≈4g` 是本图事实，可作为双栏密集矩阵的起点，不是所有任务的固定值。
- **布局收益**：常规 gutter 维持同组连续性，较大的 group gap 与分隔线共同表达结构，使读者不依赖反复阅读标签也能识别输入、预测、真值和 case 边界。
- **防误用**：扩大 group gap 会消耗结果面积；列数较多或单栏空间不足时，应减少倍数、缩短标签或改用浅色底托，而不是把每张结果压缩到不可读。

#### E04 — 使用对齐的两级表头，而不是逐图重复 caption

- **技术证据**：第一层 `Increasing Training Compute` 与水平箭头横跨五个 scaling 列；第二层 `Context`、`0.7 EFLOP`、`2.6 EFLOPs`、`5 EFLOPs`、`16 EFLOPs`、`28 EFLOPs` 和 `Ground Truth` 共享同一基线，并分别居中于对应列。第二层文字下沿与 tile 顶边保留约一个普通 gutter 量级的距离。
- **候选规则**：当多列共享一个变量时，使用“全局变量/方向层 + 具体列值层”的两级 header。所有同级 header 统一字号、基线、与 tile 的距离和水平居中方式；变量名只标一次，不在每张图中重复。
- **实现建议**：先按 tile 中心计算 header anchor，再统一设置 baseline；不要按字符串宽度手工拖动。长短不一的标签应视觉居中，但基线必须严格一致。
- **防误用**：若只有两列或变量方向已经显而易见，可以省略第一层箭头；header 层级应帮助比较，不能为了装饰侵占图像高度。

#### E05 — 侧边标签方向应服从剩余空间与行对应关系

- **技术证据**：`Ours SVSM` 与 `LVSM dec-only` 没有占用完整的独立方法列，而是以约 `50–55°` 的斜向标签放在 Ground Truth 右侧窄区，并分别对准每一结果行。标签延伸到源图右边界附近，使整图充分占用预定双栏宽度。
- **候选规则**：优先尝试水平行标签；若水平标签会显著增宽、垂直标签难读、图顶已有两级 header，或右侧只剩斜向窄区，可以旋转标签以贴合可用空间。所有方法标签使用相同角度、锚点、字号和与对应行的距离。
- **替代方案**：空间较宽时使用左侧 row header；方法较多时增加紧凑方法列；标签很短时可用水平 overlay；只有斜排真正改善 bounding box 利用率时才使用斜排。
- **可读性约束**：旋转文字在最终论文尺寸必须能顺畅阅读；不能越出裁切区、互相碰撞或与正式 caption 混淆。斜体字形与文字旋转是两件不同的设计选择，不应捆绑。

#### E06 — Figure 5 的版面完成检查

1. 同一层级的 tile 具有相同尺寸、长宽比、边框与 crop 规则；
2. 列中心、行中心、header baseline、separator 和侧边标签锚点都来自统一网格；
3. 不同 case 使用明确但不过重的分组方式；不同功能列族使用不同于 case 的分隔语法；
4. 普通 gutter、group gap、边框和 separator 采用成组 token，不逐处随意修改；
5. header 与 method 标签尽量使用图外现有窄区，不遮挡结果，也不制造大块新空白；
6. bounding box 内的空白必须承担呼吸、分组或标签功能；若既无语义又接近一个 tile 的面积，应重排；
7. 所有几何与文字在双栏实际缩放尺寸下重新渲染检查。

### 对 Qualitative Demonstration Figure 分支的更新

- Figure 5 强化了此前 Q03、Q08 和 Q11 的对齐、间距与边框规则，并新增“separator 语法”和“两级 header”组件。
- “紧凑”继续定义为高效利用目标版面、保持几何秩序，并不等于零间距；Figure 5 恰好通过约 `3.7 pt` 的规则 gutter 获得比无缝拼接更清楚的比较结构。
- 斜排标签只作为空间自适应手段收录。Skill 的默认判断顺序应是：比较语义 → 可用窄区 → 可读性 → 标签方向，而不是看到 NVS 图就自动旋转文字。

## Paper 06 — Content-Aware Texturing for Gaussian Splatting

### 文件与 Figure 映射

- **标题**：*Content-Aware Texturing for Gaussian Splatting*
- **源码目录**：`reference papers/content-aware-texturing-for-gaussian-splatting/`
- **Figure 6**：由 `sections/implementation.tex` 中的双栏 `figure*` 生成；15 张原始结果位于 `images/table1/`。
- **结构**：`3` 个 dataset/case 行 × `5` 个图像列，分别为 `Ground Truth | 2DGS* | BBSplat | GStex | Ours`；左侧另设一个窄的旋转 dataset 标签 rail。
- **双栏几何**：模板 `\textwidth=42 pc≈504 pt`；每张主图宽度设为 `.193\textwidth≈97.3 pt`，五列图像占约 `96.5%` 的双栏宽度，列间 `\tabcolsep=1.5 pt`，旋转标签利用窄侧栏完成场景说明。

### Figure 6 — NVS 对齐比较矩阵与局部质量放大 patch

#### 用户明确认可的设计点

1. 三行五列严格对齐并紧凑占满双栏；每列由统一 header 标记方法，每行由左侧旋转文字标记 dataset/case。
2. Ground Truth 位于最左图像列，并用实线与右侧四个 method 结果形成不同功能区。
3. 每张结果图都包含同一位置的局部质量放大 patch；小 ROI、放大框与连接线使用高可见度亮红色。
4. 小 ROI 框较细，放大框较粗，二者都有完整边框并通过连线建立对应关系。
5. 放大框按每个 case 的主体位置选择低遮挡角落；例如自行车 case 使用左下角，车辆 case 使用右下角，避免覆盖主体。
6. 这些规则用于 Agent 提供设计选项、可编辑草版和素材到齐后的合成，不要求 Agent 在缺少真实结果时虚构最终 Figure。

#### F01 — 将 NVS 比较组织为 `case × method` 矩阵

- **技术证据**：Figure 6 使用 `tabular{cc|cccc}`：第一列为旋转 dataset 标签，第二列为 Ground Truth，随后是四个 method。header 分别为 `Ground Truth`、`2DGS*`、`BBSplat`、`GStex`、`Ours`；三行依次为 `Mip-Nerf360`、`Deep Blending` 和 `Tanks&Temples`。
- **候选规则**：让行表示 scene/dataset/case，让列表示 Ground Truth/reference 与各 method。每个列 header 只出现一次，每个行 label 只出现一次；同一列的宽度、中心线和 header anchor 必须贯穿所有行。
- **版面策略**：当横向方法较多、而 dataset 名较长时，可把行标签旋转 `90°` 放入窄侧栏；它是节省横向空间的可选策略。若标签较短或旋转后难读，则改用水平 row header。
- **防误用**：`3×5` 是本图实例，不是 NVS 固定模板。实际行列数必须由 case 和 method 数量决定；方法过多时应拆 panel、分主文/补充材料或减少展示列，不能无限压缩图片。

#### F02 — 用实线分开 reference 区与 method 区

- **技术证据**：表格列格式中的 `|` 在 Ground Truth 后形成约 `0.4 pt` 的黑色实线，贯穿 header 与三个结果行。它把 reference/target 与所有预测方法分开，而不是给每两列都增加边线。
- **候选规则**：当 Ground Truth、input、reference 或 observation 与预测结果在语义上属于不同功能区时，在两组之间增加一条克制的实线 divider。divider 应跨越整组高度并与网格对齐。
- **防误用**：不要用大量竖线把每个 method 都关进独立格子；同类 method 之间优先靠统一 gutter 和 header 区分。若没有 Ground Truth 或 reference 区，就不应机械保留这条线。
- **证据关系**：与 Paper 05 Figure 5 的 separator 语法一致，进一步验证“实线/虚线必须表达功能层级”。

#### F03 — patch 组件使用 `ROI → connector → magnified inset` 三层线宽

- **源代码证据**：统一 macro 设置 `magnification=5`、`size=1cm`、`connect spies`，颜色为 TikZ `red`，即纯红 `#FF0000`。
- **矢量证据**：从临时重建 PDF 的 vector path 恢复到：
  - 小 ROI 框约 `0.20 pt`；
  - 连接线约 `0.40 pt`；
  - 大放大框约 `0.80 pt`。
- **候选规则**：把 `0.2 : 0.4 : 0.8 pt` 的 `1:2:4` 层级作为双栏 NVS 图的起点：ROI 尽量精细，不遮住被观察纹理；connector 清楚但退居辅助；放大框最强，建立局部结果的视觉边界。最终仍需按论文缩放尺寸复检并成比例调整。
- **尺寸证据**：放大框为 `1 cm≈28.35 pt` 方形，约占单张 `97.3 pt` 主图宽度的 `29%`；小 ROI 因 `5×` 放大约为 `5.67 pt` 方形。该比例让纹理差异可见，同时把遮挡控制在一个角落附近。
- **防误用**：不要让 ROI 与大框使用同样粗的线，也不要让 connector 比大框更抢眼。若最终尺寸下 `0.2 pt` ROI 消失，可整体放大这组比例，但仍保持小框 < connector < 大框的视觉重量。

#### F04 — 高饱和红是功能性 annotation 色，不是类别色板

- **用户证据**：patch 需要使用较亮、容易识别的红色，不能选择很浅、接近背景的红。
- **技术证据**：本图实际使用纯红 `#FF0000`，且仅用于 ROI、放大框和连接线；方法名称、dataset 标签和其他结构保持黑色。
- **候选规则**：局部质量标注优先测试高饱和 annotation red。可从源图 `#FF0000` 或全局柔和色板中的亮深红 `#F5433D` 起步，在全部 case 上检查对比度；同一 Figure 只使用一个 patch annotation 色。
- **颜色边界**：该红色属于功能标注 token，不自动加入统计图的 categorical palette，也不表示某个 method 好坏。若场景大面积为红/橙色，可加极细的白色外 halo、选择更深红，或在保证整图一致的前提下更换另一种高对比 annotation 色。
- **科研约束**：不得只给 proposed method 使用醒目红框而让 baseline 使用弱色；所有方法必须使用完全相同的标注样式。

#### F05 — 同一 case 的 ROI、倍率和 inset 位置必须跨方法锁定

- **技术证据**：每一 dataset 行中的五个 `\spyimage` 调用使用完全相同的 ROI 坐标与 inset 坐标：
  - Mip-NeRF360：`ROI=(0.4,1.5)`，`inset=(1.1,0.6)`；
  - Deep Blending：`ROI=(3,0.3)`，`inset=(3.3,1.3)`；
  - Tanks&Temples：`ROI=(3.1,1.65)`，`inset=(3.1,0.6)`。
  所有行统一使用 `5×` magnification 和 `1 cm` inset。
- **候选规则**：先在 Ground Truth 或共同 camera view 上确定一个科学上有意义的 ROI，然后把归一化 ROI 坐标、放大倍率、inset 尺寸、anchor、边框色和线宽锁定到该行所有 method。不要为每个 method 各找一个“最能表现好坏”的不同区域。
- **比较公平性**：所有 tile 必须来自同一 target view，并使用相同 crop、resize 和颜色处理。若某 method 的输出尺寸不同，应先统一坐标映射，再绘制 ROI。
- **例外**：只有当不同 method 本身输出不同模态或不存在一一对应像素时，才允许使用不同 ROI；此时必须明确标注，不应伪装成像素对齐比较。

#### F06 — inset anchor 通过主体避让选择，并在同一行保持一致

- **用户证据**：自行车 case 的大 patch 放在左下角，避免盖住自行车；底部车辆 case 的大 patch 放在右下角，避免覆盖车辆主体。
- **技术证据**：Figure 6 按 case 改变 inset anchor，但在同一行五种结果中保持相同。Deep Blending 行则把 inset 放在右上区域，说明角落选择是内容自适应的，不是全图固定一个角。
- **候选放置流程**：
  1. 标出主对象、脸、文字、细结构和科研关注区域作为 protected regions；
  2. 在四个角及必要的边缘候选区计算遮挡，排除覆盖主体或 ROI 的位置；
  3. 在剩余位置中选择遮挡低、connector 短、不会穿过主体的 anchor；
  4. 将该 anchor 锁定到同一 case 的所有 method；
  5. 若所有内部位置都不安全，把 inset 移到 tile 外的共享 zoom row/column，而不是强行遮挡。
- **防误用**：不要只在 proposed method 上精心避让、却让 baseline 的 patch 覆盖重要内容；遮挡规则必须跨列一致。放大框遮住的背景也应尽量是低信息区域，而不是另一处需要比较的纹理。

#### F07 — Agent 在草版与最终合成中的协作职责

- **只有论文叙事时**：先给可编辑 SVG/PPT/Figma 草版，画出真实行列数量、Ground Truth divider、方法 header、dataset label rail、ROI placeholder、四角 inset 候选和 connector；明确标记 `[请提供同视角结果]`、`[请选择/确认 ROI]`、`[主体保护区]`。
- **素材到齐时**：检查相机/视角对应、尺寸、crop 和颜色空间；生成统一 contact sheet；协助用户选择能展示高频纹理、细线、反射、几何边缘或 texture stretching 的 ROI；再统一绘制 patch。
- **可以主动提醒用户**：同时准备代表性 case、难例和失败模式；patch 应服务论文结论，而不是只选择 proposed method 最占优势的位置。
- **不应擅自完成的部分**：不得在用户未确认科学比较目的时替他决定最终 case 或删除失败结果；不得虚构 Ground Truth、baseline 输出或局部细节。

#### F08 — NVS patch comparison 的完成检查

1. 行列、header、dataset label、divider 与 tile 边界来自统一网格，并在双栏实际宽度下紧凑对齐；
2. 每行所有方法使用同一 target view、ROI、倍率、inset 尺寸、位置、颜色与线宽；
3. ROI 清楚指出被放大的位置，大框与小框之间存在不歧义的 connector；
4. 小 ROI 不因线宽过粗而遮住细节，大框在最终尺寸下足以分辨质量差异；
5. inset 不覆盖主体、文字、另一处关键证据或其他 annotation；
6. annotation red 在所有背景上可见，且没有被误用为 method 优劣编码；
7. bounding box 内没有无意义空白，同时保留足够 gutter，防止相邻场景和 patch 视觉粘连；
8. 草版保持可编辑，最终合成保留高分辨率图像，并优先导出矢量文字/边框/连接线与无损或高质量嵌入图片。

### 对 Qualitative Demonstration Figure 分支的更新

- 新增 NVS/neural rendering 的 **detail patch component**：小 ROI、connector、大 inset、统一 annotation 色和内容自适应 anchor 必须作为一个完整组件设计。
- “局部放大”现在分为两种：统计曲线使用带独立坐标轴的 zoomed inset；图像结果使用像素对齐的 magnified patch。两者都需要来源标记和遮挡审计，但不能混用实现语法。
- Figure 6 进一步验证 separator、旋转窄标签和双栏满宽矩阵；这些都是根据内容密度选择的工具，不把 `3×5`、纯红或 `5×` 放大写成所有结果展示图的硬性模板。

## Forward Test 04 — Results Display Test（V2 验证布局方向；仅为测试 case）

### V1 中已验证的部分

- 用户认可功能区分界线、统一黑色 tile 边框与图像局部放大 patch；这些组件可继续保留。
- 高可见度红色 annotation、同一 case 跨方法锁定 ROI/inset，以及根据主体位置选择 patch anchor 的方向符合预期。

### V1 暴露的问题与修正规则

1. **不能只追求紧凑而忽略最终 tile 尺寸**：`2 × 8` 虽然外轮廓紧凑，但放入双栏论文后单张结果过小。设计 grid 前必须按最终栏宽估算每张 tile 的物理尺寸和细节可辨性；列数过多时优先换行、嵌套分组或拆 panel。
2. **当前 16 张素材适合采用内容驱动的 `4 × 4`**：每个 case 占两行四列；第一列把 `Blurred RGB` 与 `Event Input` 分置上下两行，右侧六张 `GT + 5 methods` 组成 `2 × 3`。两个 case 纵向堆叠后形成四行四列，既保持功能分区，也让双栏中的单图显著放大。这里的 `4 × 4` 只解决本次测试素材，不能固化成通用模板。
3. **列语义变化时使用逐 tile 的短 header**：右侧 `2 × 3` 在上下行对应不同方法，不能强行套一个贯穿四行的列标题。应把短 caption 紧贴各 tile 上方并统一基线、字号和间距。
4. **ROI 与 inset 默认使用两根 connector**：单根线只能说明大致对应关系，视觉结构偏弱。优先从 ROI 的两个相邻角连接到 inset 对应边的两个角，形成清楚的梯形/透视展开关系；两线应同色同宽、不交叉、不过度穿过主体，并压在 inset 边框下方。
5. **功能 divider 随重排更新**：在每个两行 case 内，用一条贯穿两行的实线分隔左侧 input column 与右侧 comparison block；用另一条横向实线分隔两个 case。不要保留已失去分组意义的旧 separator。

### V2 实现记录

- 新版输出采用双栏 `7 in` 宽、四列四行版式；单张 tile 约占全宽的四分之一。
- Case 1 的放大 patch 放在左下角，Case 2 放在右上角；每个结果 tile 均改为双线梯形连接。
- 可编辑母版保留为 SVG，PDF 用于论文插入，PNG 用于快速预览；输出统一位于 `output/results-display-test/v2/`。
- 用户认为 V2 明显优于 V1，说明减少每行列数、扩大单图尺寸的修正方向正确；但该图只是用于测试与反馈，不代表用户要求交付一张正式最终 Figure。
- V1 中已认可的黑框、分界线与 patch 组件可视为稳定证据；V2 的具体 `4 × 4` 排列只保留为 case-level 证据。

### 从本测试提炼出的通用 Layout 决策规则

1. 先确定目标载体及实际宽度：单栏、双栏、整页或补充材料；不能只在高分辨率画布上判断“看起来放得下”。
2. 统计图片数量、长宽比和语义分组，再提出多个候选网格；不要默认把所有方法横向塞进同一行。
3. 对每个候选网格估算最终单图尺寸：`tile width = (可用宽度 − 标签 − 分界线 − 所有 gutter) / 每行图片数`。
4. 按论文实际尺寸渲染检查主体、局部纹理、patch 和 caption。只要其中任何一项变得难辨认，就应减少每行图片数，并改用换行、输入独立列、嵌套 `2 × n`、上下堆叠 case 或拆分 panel。
5. 在可读性满足之后再优化紧凑度。紧凑不是“横向放得越多越好”，而是在保持单图有效尺寸的前提下，让 bounding box 内没有无意义空白。
6. 不把本测试的 `2 × 8`、`4 × 4` 或任何固定网格写成默认答案；Skill 应保存的是上述选择过程与最终尺寸检查。

## Teaser Figure 分支 — 训练边界与 Agent 职责

### 用户对 Teaser 的定义

- Teaser 通常放在论文最上方，目标是让读者第一眼就理解论文在研究什么、核心方法或核心贡献是什么。
- 在版面和投稿规范允许时，用户倾向于为论文设计 Teaser；它承担的是论文的第一视觉入口，而不只是正文某个实验的补充说明。
- Teaser 具有很强的艺术性、叙事性和项目特异性，难以完全量化，不能像统计图那样制定大量必须机械满足的硬规则。

### 本分支采用高自由度而非固定模板

1. 从后续 reference papers 中提炼可迁移的构图思路、视觉层级、叙事顺序、配色关系、素材组织和空间利用方式；不复制某张图的具体物体、位置或造型。
2. 将观察结果记录为设计选项、适用条件和防误用说明，而不是“所有 Teaser 都必须如此”的规则。
3. 同一论文可提出多个方向明显不同的 concept，例如结果主导、问题—方法—结果、输入—变换—输出或场景叙事；不要过早收敛到唯一构图。
4. 评价重点首先是读者能否迅速看懂论文主旨，其次才是装饰性和视觉冲击力。艺术性不能以牺牲信息清晰度为代价。

### Agent 的默认交付边界

- 默认扮演设计协作者和视觉导演：先理解论文的一句话核心信息、输入输出、关键创新、最有说服力的结果以及目标版面。
- 优先给用户构图概念、草版 layout、视觉动线、层级说明、色彩方向和素材清单，并标出需要用户补充或确认的中间结果、渲染图、对比图或代表性 case。
- 草版应保持可编辑，方便用户在 Figma、PPT、Illustrator 或其他工具中继续修改；在没有足够真实素材和用户确认时，不把草版冒充最终成图。
- 用户提供素材后，可以继续协助裁切、对齐、合成、配色和细节润色；最终内容选择与科研叙事仍需和用户共同确定。
- 只有用户明确要求并提供充分素材时，才尝试制作接近最终版的 Teaser；即使如此，也应先给 concept/layout 供用户确认。

### 后续学习记录方式

- 对每篇 reference paper 记录：Teaser 想让读者首先看到什么、视觉焦点在哪里、阅读顺序是什么、各区域承担什么叙事功能、哪些素材不可由 Agent 虚构，以及用户明确认可的美学细节。
- 将反复出现且跨论文有效的规律逐步提升为候选原则；只在多次 reference 或 forward test 中得到验证后，才写成稳定规则。

## Paper 07 — Alchemist: Parametric Control of Material Properties with Diffusion Models

### 文件与 Figure 映射

- **标题**：*Alchemist: Parametric Control of Material Properties with Diffusion Models*
- **源码目录**：`reference papers/alchemist-parametric-control-of-material-properties-with-diffusion-models/`
- **Figure 1 / Teaser**：`figures/source/teaser_2_2.pdf`，由 `figures/tex/teaser.tex` 以 `width=\linewidth` 插入。
- **画布证据**：Teaser PDF 为 `495 × 289.814 pt`，恰好按 CVPR 双栏正文宽度设计；源文件由 Adobe Illustrator 28 创建，说明图像、文字、横线和箭头是在统一视觉画布中共同排版，而不是逐图由 LaTeX 临时拼接。

### Figure 1 — 用“离散编辑 + 连续控制 + 多样案例”讲清论文价值

#### 用户明确认可的设计点

1. Teaser 在最短时间内直接说明论文做什么以及为什么有意义：使用 diffusion 控制 `Roughness`、`Metallic`、`Albedo` 和 `Transparency` 等材料属性。
2. 上面两行以 `Input → Output` 配对展示直接编辑效果；下面两行以每个 case 五张图的序列展示连续强度变化，进一步说明方法像滑条一样支持参数化渐进控制。
3. 各行图片数量和高度并不完全相同，但所有内容共享严格一致的左右边界；文字、箭头和行间空隙都承担功能，没有无意义的大块留白。
4. Case 在对象类别上覆盖动物、金属、陶瓷/陶器、玩偶、家具、鞋子等，在视觉色彩上形成橙、绿、黄、蓝、灰白等对比，帮助展示方法的广泛适用性和说服力。

#### T01 — 先用“一眼可复述”检验 Teaser 是否紧扣核心

- **本图叙事**：读者即使只快速扫过，也能看到四种材料属性、输入到输出的变化，以及连续控制序列，从而复述“该方法可以控制真实图像中的材料属性，并且控制强度是连续可调的”。
- **候选规则**：开始排版前先写一句希望读者看完 Teaser 后能复述的话，再只保留支持这句话的视觉证据。Teaser 不应尝试概括论文的每个模块、损失函数和实验结论。
- **Agent 检查问题**：`做了什么操作？控制了什么变量？核心优势是什么？` 如果视觉本身无法回答其中最重要的两项，就应先调整素材与叙事，而不是继续增加装饰。

#### T02 — 用由浅入深的两层证据结构降低认知负担

- **第一层：离散 mapping**。上面两行使用多个 `Input / Output` pair，让读者先理解“输入对象经过方法后，指定材料属性发生变化”。这种二元关系阅读成本最低。
- **第二层：连续 controllability**。下面两行把同一对象在多个强度值下并排，并使用 `-1 → +1` 或 `0 → +1` 的方向标记，说明输出不是单次风格转换，而是可以沿属性轴平滑变化。
- **候选规则**：当论文既有基础能力又有更强性质时，可让 Teaser 先给最容易理解的输入输出关系，再用第二层展示连续性、可编辑性、泛化性、时序一致性或其他核心优势。
- **防误用**：层级必须递进而非重复。如果第二层只是换一个对象再次展示相同的一步编辑，就不值得占据 Teaser 的大量面积。

#### T03 — 允许不同内容带使用不同网格，但锁定共同外轮廓

- **技术证据**：上面两行各包含六张较宽图片，下面两行各包含两个五帧序列、合计十张较窄图片；四条内容带的左右边界仍对齐到同一 `495 pt` 满宽画布。
- **候选规则**：不要要求整个 Teaser 只能使用一个全局等宽 grid。可以按叙事功能让不同 band 使用 `3 × 2` pair、`2 × 5` sequence 或其他局部网格，但每条 band 应共享明确的左右锚点，并通过比例计算使总宽度一致。
- **布局公式**：对每条 band 分别满足 `Σ tile widths + Σ gutters + label rails = common content width`；先确定共同宽度，再反推各自 tile 尺寸。
- **防误用**：共同宽度不是把每行强行拉伸到变形。若源图长宽比不兼容，应裁切、重选素材、调整 case 数或拆分叙事，而不是非等比缩放图像。

#### T04 — 让行间文字、横线和箭头同时承担分组与解释

- **技术证据**：`Roughness`、`Metallic`、`Albedo`、`Transparency` 等属性名位于细横线的断口中；`Input`、`Output` 紧贴对应图列；连续序列使用带数值端点的水平箭头标出控制方向。
- **候选规则**：优先把短标题、变量范围和方向信息放进原本就需要的窄行间区域，使文字成为布局结构的一部分。细横线用于建立属性分组，箭头用于表达控制轴，不作为随机装饰。
- **紧凑含义**：可以保留少量呼吸空间，但每个明显 gap 应至少承担分组、标签、方向提示或避免粘连中的一种功能。
- **防误用**：标签数量多或语句很长时不要硬塞进图间；Teaser 内文字应短而可扫读，详细解释交给正式 caption。

#### T05 — Case 选择同时覆盖“科研语义”与“视觉节奏”

- **语义覆盖**：用不同对象类别、材质基础、背景环境和属性类型，帮助读者判断方法并非只对单一对象或单一材料有效。
- **视觉覆盖**：相邻 case 有意识地形成橙、绿、黄、蓝、灰白和深色之间的对比，使读者能快速区分组别，也让整图产生节奏。
- **候选流程**：先按论文 claim 建立必须覆盖的语义矩阵，再在每个语义格中选择色彩、轮廓和背景互相区别的代表性结果。美学选择发生在满足科学代表性之后。
- **Agent 可主动建议**：避免整行都是近似白色、近似黑色或同一背景；优先让相邻 case 在主色、形状和对象类别上都有至少一个清楚差异。
- **科研边界**：不能为了颜色好看而改变方法输出、伪造结果或只挑 proposed method 最有利的 case。代表性、难例和局限性仍需在正文或补充材料中诚实呈现。

#### T06 — 本图的具体数量只作为构图实例

- `6 / 6 / 10 / 10` 的四行密度、四种材料属性、五级滑条和具体对象都属于 Alchemist 的论文叙事，不写成 Teaser 的固定模板。
- 可迁移的是：一句话核心 → 低门槛直接证据 → 更强性质证据 → 语义与色彩兼顾的案例选择 → 不同局部网格共享统一外轮廓。
- Agent 为新论文设计时应先提出与论文 claim 对应的内容层级，再决定行数、每行 case 数、是否使用序列，以及哪些位置需要用户补充真实结果。

## Paper 08 — Soft Anisotropic Diagrams for Differentiable Image Representation

### 文件与 Figure 映射

- **标题**：*Soft Anisotropic Diagrams for Differentiable Image Representation*
- **源码目录**：`reference papers/soft-anisotropic-diagrams-for-differentiable-image-representation/`
- **Teaser**：`Figs/teaser.pdf`，由 `main.tex` 的 `teaserfigure` 环境以 `width=\textwidth` 插入。
- **源文件结构**：Teaser PDF 画布为 `2344 × 1140 pt`，内部嵌入一张 `4688 × 2280 px`、`144 ppi` 的 JPEG；因此图中文字已栅格化，PDF 不包含可识别的字体对象。论文 `acmart.cls` 在依赖可用时采用 Libertine/Libertinus Math，并使用 Inconsolata 作为等宽字体，可作为 SIGGRAPH/ACM 学术排版的字体参考，但不能据此断言 Teaser 内部标签的精确字体。

### Teaser — 用公平的质量与效率对比作为第一视觉论据

#### 用户明确认可的设计点

1. 左侧三列分别展示两个 baseline 与 proposed method；每列都由 reconstructed image、error map、method name、PSNR 和 running time 构成，结构严格一致。
2. 最右侧使用 proposed method 的大幅全景结果。左侧列下方需要三行文字，而右侧只有一个 `Ours` 标题，因此作者放大右侧标题字号，使不同信息量的 caption band 在视觉重量上仍然平衡。
3. 该任务属于已有较多 baseline 的经典 Differentiable Image Representation；Teaser 通过同行对比、error map、PSNR 和时间，直接证明方法在重建质量与效率上的优势。
4. 与 Alchemist 的能力展示型 Teaser 不同，本图属于比较证明型 Teaser。选择哪一种策略应取决于任务成熟度、baseline 情况和最有说服力的论文 claim。
5. SIGGRAPH/ACM 风格的整体字体与字级层次具有较高审美价值，值得作为学术图字体方向参考，即使论文并非投稿 SIGGRAPH，也可借鉴其克制、清晰的排版气质。

#### T07 — 先根据任务属性选择 Teaser 的证据模式

- **能力展示型**：任务新颖、baseline 很少、主要贡献是以前无法实现的新能力时，优先用多样的 proposed outputs、输入输出关系和可控维度回答“这个方法能做什么”。Alchemist 是当前 reference。
- **对比证明型**：任务成熟、baseline 明确、贡献主要体现在质量、速度、压缩率或资源效率时，优先在公平设置下并排展示 baseline 与 ours，并辅以能被快速理解的局部误差和关键指标。本篇是当前 reference。
- **直觉—结果型**：当输出本身不足以让读者理解论文的新意，而核心方法可以被压缩成一个简单直觉时，用上层解释最关键的“为什么/怎么做”，下层展示真实结果回答“能做到什么”。3DPR 是当前类型 reference；详见 Paper 09。
- **能力—对比组合策略**：若论文同时有明显的新能力与成熟 benchmark，可用一个 hero result 讲能力，再用一个紧凑 comparison strip 提供可信度；它是前两种证据的组合方式，不等同于上述“直觉—结果型”。必须明确唯一主叙事，不能让两套故事争夺注意力。
- **防止二分法僵化**：是否存在 baseline 不是唯一判断标准。最终应选择最能支持论文首要 claim、且能在数秒内被视觉理解的证据模式。

#### T08 — 比较型 Teaser 使用同构列建立可扫描证据栈

- **技术证据**：左侧三列共享相同宽度、相同 crop、相同上下分区和相同 caption band。每列依次为重建结果、error map、方法名、PSNR 与运行时间。
- **候选规则**：让每个 method column 使用同一信息顺序与几何结构，读者只需理解一次列语法即可横向比较。方法名、质量指标和效率指标分别占固定基线，不随字符串长度上下漂移。
- **视觉层级**：重建图回答“看起来如何”，error map 回答“误差在哪里”，PSNR 回答“总体质量多高”，running time 回答“代价是多少”。多种证据互补，但每种只保留一个最能支持主 claim 的指标。
- **防误用**：不要为 proposed method 添加 baseline 没有的有利信息，也不要让 baseline 图更小、crop 更差或 error map 更醒目。强调应来自结果本身与清楚的层级，而不是不公平的图形处理。

#### T09 — Error Map 必须作为统一测量工具，而不是装饰性热图

- **论文证据**：正式 caption 明确说明 error maps 位于 bottom row，并使用 `2× scaled` 显示；三种方法在同一位置比较边缘和结构误差。
- **候选规则**：所有方法必须使用同一 reference、像素对齐、误差定义、动态范围、缩放系数和颜色映射。若使用倍率增强，必须在 Figure caption 或图内简洁标明。
- **选择区域**：优先选择高频文字、细边缘、结构边界或重复纹理等能够暴露重建差异的位置；区域必须由科学比较目的决定，并跨方法锁定。
- **防误用**：禁止为每个方法自动拉伸各自 error map 范围；这会让颜色不可横向比较。也不能只显示 proposed method 的低误差区域而避开其失败区域。

#### T10 — 用全景列与 ROI 连接解释比较 crop 的上下文

- **技术证据**：右侧大图展示 proposed method 的完整场景；蓝色 ROI 框与两条蓝色虚线把全景中的局部区域连接到左侧比较区域。左侧 `Ours` 重建图也使用同色边框建立对应关系。
- **候选规则**：当局部 crop 最能显示方法差异、但脱离全景后难以理解时，可增加一张上下文大图，并通过一致颜色的 ROI 与双线/虚线 connector 建立映射。
- **布局收益**：大图同时提供视觉吸引力、场景语境和局部比较来源；它不是为了单纯把 ours 放得更大。Baseline 仍需在左侧获得相同尺寸的可比 crop。
- **防误用**：若全景列会使 baseline 过小或占用过多版面，应改用共享 context strip、独立 inset 或减少指标；不能为了 hero image 牺牲比较可读性。

#### T11 — 信息行数不同时进行光学对齐

- **本图问题**：左侧每列 caption band 包含三行：方法名、PSNR、时间；右侧只有 `Ours (2.0 BPP)` 一行。如果全部使用相同字号并按顶边对齐，右侧会显得空、轻且失去共同基线感。
- **本图处理**：扩大右侧单行标题，并把它垂直放在与左侧三行 stack 对应的 caption band 中，使两侧视觉重量和底部轮廓平衡。
- **候选规则**：先为所有列定义相同高度的 caption band，再按信息量选择字号、行距和垂直中心。单行标签可以适度增大，或使用隐形占位/副标题补齐层级；目标是光学平衡而非逐字符机械对齐。
- **防误用**：不能仅因为是 proposed method 就任意放大字体。字号变化必须解决真实的结构不平衡，并在最终论文尺寸下仍保持层级克制。

#### T12 — 将 SIGGRAPH/ACM 字体气质收录为优先候选，而非硬绑定投稿 venue

- **模板证据**：本论文的 `acmart.cls` 优先使用 Libertine/Libertinus Math 字体栈，图注和部分层级采用 sans-serif；整体呈现为高可读、字面开阔、字重克制的学术风格。
- **Teaser 证据限制**：`Figs/teaser.pdf` 是单张 JPEG，无法从 PDF 中恢复内部字体名称。因此只记录视觉特征，不虚构具体字族。
- **候选方向**：Teaser 的 method label 和 metric 优先测试干净的学术 sans-serif，并使用少量字级建立层级；正文/公式字体则与论文模板协调。后续如获得可编辑源文件，再补充精确字体与字号。
- **通用性**：即使不是 SIGGRAPH 投稿，也可以借鉴这种字体气质；但必须遵守目标 venue 的模板要求，并避免在同一 Figure 中混用过多字族。

### Teaser 模式选择的当前候选流程

1. 用一句话确定论文最重要的 claim；
2. 判断读者最需要先理解的是“新能力存在”“我们在成熟任务上明显更优”，还是“方法背后的关键直觉”；
3. 若选择能力展示型，规划能力维度、输入输出关系和案例覆盖；
4. 若选择对比证明型，先确定公平的 matched setting，再规划同构 method columns、误差证据和关键指标；
5. 若选择直觉—结果型，只保留一个最小可理解的机制图，并明确它与下方结果之间的因果或功能关系；
6. 若使用全景 hero image，确保它同时承担上下文或叙事功能，而非只用于放大 ours；
7. 最后统一字体、caption band、外轮廓和最终尺寸可读性，并明确需要用户提供的真实结果与实验条件。

## Paper 09 — 3DPR: Single Image 3D Portrait Relighting with Generative Priors

### 文件与 Figure 映射

- **标题**：*3DPR: Single Image 3D Portrait Relighting with Generative Priors*
- **源码目录**：`reference papers/3dpr-single-image-3d-portrait-relighting-with-generative-priors/`
- **Teaser**：`figures/teaser/teaser_3.png`，尺寸为 `5649 × 2047 px`、RGBA，由 `main.tex` 的 `teaserfigure` 以 `0.90\linewidth` 插入。
- **正式叙事**：caption 说明方法从单张 portrait 预测 One-Light-At-a-Time（OLAT）reflectance basis，再按 HDRI 线性组合进行 relighting，并把 OLAT 渲染到新相机视角以支持 3D-consistent portrait relighting。

### Teaser — 第三种“核心直觉 + 输出能力”叙事模式

#### 用户对本图的定位

- 这张图的代表性在于叙事类型，而不代表其整体美感已经达到优秀 reference 水平。
- 它既不是只展示 proposed outputs 的能力型 Teaser，也不是与 baseline 并排比较的证明型 Teaser。
- 上半部分用最简单的图像算式和箭头解释 `Additive Light Transport → Relighting` 的核心直觉；下半部分再展示 `Relighting and Novel View Synthesis` 的实际输出。
- 用户不认可两项视觉执行：左侧单张 Input 没有填满上下内容带造成明显空白；部分红绿混合结果的颜色不够美观。

#### T13 — 直觉—结果型 Teaser 只解释一个最关键机制

- **本图结构**：上层使用 `O₁ + O₂` 与带颜色权重的组合关系说明 OLAT/light transport 可以线性组合得到新的 illumination；下层使用多个相机视角与光照结果展示 relighting 和 novel-view synthesis。
- **候选规则**：把整篇方法压缩为一个读者无需公式即可理解的 visual sentence，随后立即用真实输出证明该直觉能带来什么能力。机制区回答“为什么/怎么做”，结果区回答“所以能做什么”。
- **与 pipeline Figure 的区别**：Teaser 中的 intuition diagram 不是完整架构图。只保留一个关键算子、关系或中间表示；训练细节、网络模块、损失和多条分支留给 Method Figure。
- **适用条件**：当论文的输入输出看起来像已有任务、但真正创新来自新的表示、组合规律或物理/几何直觉时，这种模式尤其有效。
- **失败条件**：如果核心机制无法在一个短视觉句子中解释，强行塞入 Teaser 会导致信息过载；此时应回到能力展示型，或只用一句短标签暗示方法直觉。

#### T14 — Intuition 与 Results 必须形成直接叙事闭环

- 上层展示的中间量、组合关系和符号必须在下层结果中得到对应：例如上层解释光照基的线性组合，下层就展示不同光照与视角下的实际输出。
- 阅读顺序应清楚：`Input → method/representation intuition → output capabilities`。箭头、对齐和重复视觉元素应帮助读者建立这一链条。
- 不应把一个“看起来像方法图”的装饰模块放在上面、再把无关的漂亮结果放在下面。两层必须共同支撑同一句论文 claim。
- Agent 草拟时需要标注哪些是真实 input、哪些是用户必须提供的 intermediate result、哪些是最终 output；不得虚构能改变科研含义的中间表示。

#### T15 — 跨两条内容带的 Input rail 也必须填满共同高度

- **技术证据**：右侧主体明确分为上方 intuition band 与下方 results band，但最左侧只有一张较矮的 Input，垂直居中后在其上方和下方留下大面积无功能空白。源 PNG 的主要内容约占 `y=60...1983`，而 Input 只覆盖中部的一段高度。
- **用户改进建议**：在 Input 区再加入一张有意义的图，使左侧 rail 能与上下两条内容带共同对齐并被撑满。
- **候选修复方式**：增加第二个输入/视角；让 input 与辅助条件上下堆叠；让一张更高的 input 跨两行；或把 input 放进上层、把必要的 condition/legend 放进下层。选择必须由论文语义决定。
- **检查规则**：从整图 bounding box 审计每个边缘 rail。若一侧存在接近半个 tile 以上、且不承担标签、分组或呼吸作用的连续空白，应重新分配内容，而不是仅移动中心位置。
- **防误用**：不能为了填空白随意添加无关图片。新增内容必须帮助理解输入、条件、视角、光照或结果来源。

#### T16 — 科学含义正确不代表配色已经达到审美 reference

- **用户反馈**：上层部分红绿混合的 `O₁/O₂` 或组合结果在视觉上不够美观，因此本图的具体红绿配色不进入优先色板。
- **候选改进**：若颜色只是示意不同 basis/weights，优先从已经验证的和谐双色组中选择，并同时使用标签、位置或符号编码；若颜色来自真实照明结果，则优先换一个同样能证明结论、但色彩关系更协调的 case，而不是事后篡改结果。
- **可访问性提醒**：红—绿是常见的色觉辨识风险组合。若科研语义必须使用红绿，需提高明度差、增加文字/形状编码，并在灰度或色觉模拟下检查可辨性。
- **证据边界**：只学习“用不同颜色表示可组合光照分量”的叙事功能，不学习本图当前的具体色值与混色效果。

### 本篇的证据等级

- **稳定候选**：将 Teaser 组织为最小核心直觉与真实输出的上下叙事闭环。
- **需要改进后再使用**：左侧 rail 的垂直占用、整体 bounding-box 紧凑度和 basis/mixture 配色。
- **不作审美结论**：本篇不能因为类型典型就整体标记为“优美 Teaser”；Skill 必须分别记录构思价值与视觉执行质量。

## Graphics / SIGGRAPH 配色学习阶段 — 存储与组合规则

### 用户偏好与适用范围

- 用户明确偏好 Graphics / SIGGRAPH 社区常见的配色风格，并希望把后续指定 Figure 中的颜色作为高优先级候选。
- `Graphics / SIGGRAPH` 只记录颜色的来源和审美筛选渠道，不表示这些颜色只能用于 Graphics 论文，也不表示它们只适合 Graphics 任务。
- 一旦某个颜色或组合经过用户认可，它就进入全局学术绘图优先库：无论论文投稿 CVPR、ICLR、NeurIPS、SIGGRAPH 或其他 venue，也无论任务属于 Graphics、Vision、ML 或其他方向，都应优先考虑。
- 该偏好是跨 Figure 类型共享的：统计图、Pipeline、神经网络结构图、Teaser 和结果展示图都应优先查询同一颜色库，而不是各自维护互不兼容的色板。
- “Graphics 风格”作为用户的全局默认审美 bias 记录，不宣称为客观上的唯一最优答案；最终仍需服从语义、背景、可读性和投稿模板，但不能因为目标论文不是 SIGGRAPH 就自动跳过这套优先色板。

### 颜色提取顺序

1. 优先从 SVG、TikZ、Matplotlib/绘图代码、Illustrator 导出的矢量对象或 PDF fill/stroke 中读取精确色值；
2. 若只有 raster Figure，先裁出用户指认的图形区域，排除照片、渲染物体、白底、阴影、文字抗锯齿和压缩噪声；
3. 在 Lab/OKLCH 等感知色彩空间中聚类或对平坦区域取稳健中位数，不以单个像素作为最终色值；
4. 透明区域同时记录 base color、alpha、背景以及合成后的 appearance；如果无法可靠反推出 base color，必须降低 confidence 并明确标为估计；
5. 将提取值重新渲染为 swatch，与原 Figure 并排视觉复核后再进入候选库。

### 单色记录不等于配色完成

- 每个颜色记录 `HEX / RGB / OKLCH / alpha`、来源论文与 Figure、提取方法、置信度、适用角色和证据状态。
- 同一个 hue 的不同透明度或明度变体归入同一 family；不要为了数量而把每个抗锯齿像素或透明度结果都登记成独立颜色。
- 真实照片或生成结果中的物体颜色通常不属于“画图色板”；只有用户明确指认，或该颜色属于边框、箭头、模块、曲线、背景、区域填充等设计元素时才提取。

### Combination 是优先选择单位

- 用户在同一 Figure 中共同指认的颜色构成一个 combination，并记录主色、辅助色、accent、neutral、背景、文字色及其角色映射。
- 同时记录大致使用比例、明暗层级、透明度关系和适用 Figure 类型；组合的美感往往来自这些关系，而不是 Hex 列表本身。
- 后续画图一旦选择某个已存颜色，应先查询其 combination membership，并优先使用同一组合中的 companion colors。
- 一个颜色可以属于多个组合；应根据 Figure 类型、背景和语义角色选择对应组合，不能把它所有的配套色一次性混在一起。
- 不随意跨组合拼色。确需混合时，先检查色相关系、明度层级、面积比例、文字对比、灰度区分和色觉可访问性。

### 证据状态

- `candidate`：已提取但用户尚未明确认可；
- `user-approved`：用户明确指出颜色或组合好看；
- `validated`：在 forward test 中复现并获得正面反馈；
- `preferred`：跨多篇 reference 或测试反复获得认可，可作为默认优先候选。

### 存储位置

- 结构化颜色与组合库存储在 `graphics-color-library.yaml`。
- 当前文件继续记录每篇论文的审美理由、适用条件和防误用说明；最终 Skill 只保留简洁的选择流程，并把详细色值库作为按需加载的 reference。

## 统计图字体对照测试与用户偏好（2026-07-19）

### 控制变量测试

- 使用同一张单栏统计图对照七种字体；数据、画布尺寸、坐标范围、完整边框、Grid、P1 配色、线宽、marker、legend 和标注位置保持一致，只改变字体家族。
- Candidate 映射：A = Arial，B = DejaVu Sans（常见 Matplotlib/Seaborn 默认），C = Optima，D = Helvetica Neue，E = Avenir，F = Gill Sans，G = Futura。
- Candidate C 就是 Optima；用户分别强调“Optima”和“Candidate C”均非常喜欢，因此记录为对同一字体的双重强认可，而不是两种独立字体。

### 用户确认的优先级

1. **最高优先**：Optima。用户认为其最有质感、最“起范儿”；统计图不再把 Optima 只限制为 Pipeline/Teaser 参考。
2. **高优先表达型**：Futura（Candidate G）。用户非常喜欢其个性，即使它不完全接近常规论文默认字体也应保留。
3. **高优先人文型**：Gill Sans（Candidate F）。用户明确评价为非常好。
4. **认可的中性候选**：DejaVu Sans、Helvetica Neue、Avenir（Candidates B/D/E）均获得正面反馈，可根据可移植性、标签密度和 venue 气质选择。
5. **保守回退**：Arial（Candidate A）被认为最普通、最缺少质感，但仍可在其他候选被用户否定、环境不可用或兼容性要求较高时使用。

### Skill 规则

- 统计图默认优先检查 Optima；不要因为 Arial 常见就自动把它放在第一位。
- Futura 不作为无条件自动 fallback：它是强偏好的显式 profile，适合短标签、较疏的刻度和紧凑而不拥挤的图，必须在最终论文尺寸检查小字与 legend 宽度。
- 默认自动字体栈采用 `Optima → Gill Sans → Helvetica Neue → Helvetica → Avenir → DejaVu Sans → Arial`。DejaVu Sans 保留为服务器上最可靠的可嵌入 fallback，Arial 放到最后。
- 专有系统字体只按 family name 引用，不随可移植 Skill 打包字体文件。必须记录最终 resolved font，并检查 PDF/SVG 是否发生替换。
- 同一 pt 值在不同字体下的视觉大小并不一致。切换字体后要重新检查字号、字重、字距、legend 宽度、tick 密度和数学符号；不能只替换 `font.family` 就结束。
