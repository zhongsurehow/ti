# At the very top of your script
from manim import *
import random
import numpy as np # Import numpy for np.isnan, np.isinf, np.clip

# Configure TexTemplate for Chinese characters
ctex_template = TexTemplate(
    tex_compiler="xelatex",
    output_format=".xdv",
    preamble="""
\\usepackage{amsmath}
\\usepackage{amssymb}
\\usepackage{fontspec}
\\usepackage{xeCJK}
\\setCJKmainfont{SimSun} % CRITICAL: Change to a Chinese font available on your system if SimSun is not.
"""
)

# Helper function
def parse_time(time_str):
    h, m, s_ms = time_str.split(':')
    s, ms = s_ms.split(',')
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000.0

class InformationOverloadViz(Scene):
    def construct(self):
        MathTex.set_default(tex_template=ctex_template)
        Tex.set_default(tex_template=ctex_template)
        Text.set_default(font="SimSun") # CRITICAL: Ensure this font is available to Manim's Text object

        subtitles = [
            {"id": 1, "start": "00:00:00,233", "end": "00:00:02,333", "text": "你不是信息焦虑"},
            {"id": 2, "start": "00:00:03,133", "end": "00:00:06,333", "text": "是你一直在拿漏斗接瀑布"},
            {"id": 3, "start": "00:00:06,900", "end": "00:00:09,966", "text": "现在的信息世界，像水一样"},
            {"id": 4, "start": "00:00:09,966", "end": "00:00:12,066", "text": "流得快、流得急"},
            {"id": 5, "start": "00:00:12,833", "end": "00:00:15,066", "text": "你以为你能接住所有水"},
            {"id": 6, "start": "00:00:15,366", "end": "00:00:18,933", "text": "结果只是被淹没、灌满、呛住"},
            {"id": 7, "start": "00:00:19,533", "end": "00:00:21,566", "text": "所以，聪明人不去“接”"},
            {"id": 8, "start": "00:00:22,200", "end": "00:00:25,133", "text": "而是建一个有“阀门”的系统"},
            {"id": 9, "start": "00:00:25,366", "end": "00:00:30,033", "text": "🌱《Liya的智慧锦囊》今天送你三个\n“认知止水阀”"},
            {"id": 10, "start": "00:00:30,166", "end": "00:00:32,966", "text": "第一个阀门：开局过滤法"},
            {"id": 11, "start": "00:00:33,033", "end": "00:00:35,166", "text": "别一睁眼就刷手机"},
            {"id": 12, "start": "00:00:35,300", "end": "00:00:36,733", "text": "你的第一口信息"},
            {"id": 13, "start": "00:00:36,733", "end": "00:00:39,266", "text": "决定一天的认知基调"},
            {"id": 14, "start": "00:00:40,000", "end": "00:00:42,666", "text": "建议：醒来后的前10分钟"},
            {"id": 15, "start": "00:00:42,800", "end": "00:00:45,400", "text": "只接收你主动选择的内容"},
            {"id": 16, "start": "00:00:45,600", "end": "00:00:49,266", "text": "比如一本书、一条理念、一个目标"},
            {"id": 17, "start": "00:00:49,733", "end": "00:00:52,600", "text": "🧭第二个阀门：主题感知锚"},
            {"id": 18, "start": "00:00:52,833", "end": "00:00:55,766", "text": "每天设置一个“今日关键词”。"},
            {"id": 19, "start": "00:00:56,200", "end": "00:00:58,400", "text": "遇到信息，问自己一句："},
            {"id": 20, "start": "00:00:58,800", "end": "00:01:01,633", "text": "这和我今天的关键词有关吗？"},
            {"id": 21, "start": "00:01:01,633", "end": "00:01:02,533", "text": "不相关？"},
            {"id": 22, "start": "00:01:02,533", "end": "00:01:04,466", "text": "就滑走，不内耗"},
            {"id": 23, "start": "00:01:04,633", "end": "00:01:07,600", "text": "比如今天的关键词是“专注”，"},
            {"id": 24, "start": "00:01:07,900", "end": "00:01:10,866", "text": "那你就别看跟八卦有关的一切"},
            {"id": 25, "start": "00:01:10,966", "end": "00:01:14,033", "text": "🧼第三个阀门：睡前清理池"},
            {"id": 26, "start": "00:01:14,033", "end": "00:01:16,333", "text": "不是看完信息才安心"},
            {"id": 27, "start": "00:01:16,433", "end": "00:01:20,400", "text": "而是清完“信息残留”才真的安静"},
            {"id": 28, "start": "00:01:20,566", "end": "00:01:22,166", "text": "临睡前5分钟"},
            {"id": 29, "start": "00:01:22,200", "end": "00:01:26,000", "text": "在脑中对今天的信息流“排个序”："},
            {"id": 30, "start": "00:01:26,233", "end": "00:01:28,866", "text": "什么值得记，什么该删"},
            {"id": 31, "start": "00:01:29,033", "end": "00:01:31,866", "text": "每天用一点点“认知整理术”，"},
            {"id": 32, "start": "00:01:32,133", "end": "00:01:36,633", "text": "你的大脑就不会像积水的盆——发霉、长菌"},
            {"id": 33, "start": "00:01:37,400", "end": "00:01:38,366", "text": "💡Liya提醒："},
            {"id": 34, "start": "00:01:38,733", "end": "00:01:40,000", "text": "信息是水"},
            {"id": 35, "start": "00:01:40,100", "end": "00:01:42,133", "text": "你要做的，不是接更多"},
            {"id": 36, "start": "00:01:42,133", "end": "00:01:44,000", "text": "而是疏导有序"},
        ]

        current_scene_time = 0
        active_visuals = VGroup() 
        subtitle_mobj = Text("", font_size=30).to_edge(DOWN, buff=0.5)
        self.add(subtitle_mobj)

        self.valve_icons = VGroup()
        self.valve_nums = VGroup()
        self.keyword_text_mobject = None # Will store the Tex mobject for "关键词?" or "专注"

        for item in subtitles:
            start_time = parse_time(item["start"])
            end_time = parse_time(item["end"])
            duration = end_time - start_time
            text_content = item["text"]

            if start_time > current_scene_time:
                self.wait(start_time - current_scene_time)
            current_scene_time = start_time

            new_subtitle_text = Text(text_content, font_size=30).to_edge(DOWN, buff=0.5)
            text_appear_time = min(0.5, duration * 0.2)
            self.play(Transform(subtitle_mobj, new_subtitle_text), run_time=text_appear_time)
            
            anim_duration = duration - text_appear_time
            if anim_duration < 0.1: anim_duration = 0.1 

            if active_visuals:
                self.play(FadeOut(active_visuals, shift=DOWN*0.2), run_time=0.2)
                anim_duration = max(0.1, anim_duration - 0.2)
                active_visuals = VGroup()
            
            if item["id"] == 1:
                meter_outline = Rectangle(width=4, height=0.5, color=WHITE).shift(UP)
                meter_fill = Rectangle(width=0.01, height=0.5, color=RED, fill_opacity=0.8).align_to(meter_outline, LEFT)
                percentage = DecimalNumber(0, num_decimal_places=0, unit=r"\%")
                percentage.next_to(meter_outline, RIGHT)

                def percentage_updater_id1(mob):
                    current_outline_width = meter_outline.width
                    current_fill_width = meter_fill.width
                    val_to_set = 0
                    if abs(current_outline_width) >= 1e-9: # Avoid division by zero
                        val_to_set = (current_fill_width / current_outline_width) * 100
                    
                    if np.isnan(val_to_set) or np.isinf(val_to_set):
                        mob.set_value(0) 
                    else:
                        mob.set_value(np.clip(val_to_set, 0, 100))
                    mob.next_to(meter_outline, RIGHT)

                percentage.add_updater(percentage_updater_id1)
                
                active_visuals.add(meter_outline, meter_fill, percentage)
                self.play(Create(meter_outline), Create(meter_fill), Write(percentage), run_time=min(0.8, anim_duration*0.4))
                
                original_meter_fill_height = meter_fill.height
                self.play(
                    meter_fill.animate.set_width(meter_outline.width * 0.99)
                              .set_height(original_meter_fill_height)
                              .align_to(meter_outline, LEFT),
                    run_time=min(1.0, anim_duration*0.6)
                )

            elif item["id"] == 2:
                funnel_top = Line(LEFT*0.3, RIGHT*0.3).shift(UP*0.3)
                funnel_side1 = Line(LEFT*0.3+UP*0.3, DOWN*0.3)
                funnel_side2 = Line(RIGHT*0.3+UP*0.3, DOWN*0.3)
                funnel_neck_out = Line(DOWN*0.3, DOWN*0.6)
                funnel = VGroup(funnel_top, funnel_side1, funnel_side2, funnel_neck_out).scale(1.5).shift(UP*0.5)
                num_receiver = MathTex(r"1\text{x}").scale(0.7).next_to(funnel, DOWN, buff=0.2)
                
                waterfall_source_width = 5
                num_dots = 200
                waterfall_dots = VGroup(*[
                    Dot(radius=0.025, color=BLUE_C, fill_opacity=0.7)
                    .move_to(UP*3.5 + RIGHT*random.uniform(-waterfall_source_width/2, waterfall_source_width/2)) 
                    for _ in range(num_dots) 
                ])
                num_source = MathTex(r"10000\text{x}").scale(0.7).next_to(waterfall_dots, UP, buff=0.2)

                active_visuals.add(funnel, waterfall_dots, num_receiver, num_source)
                self.play(Create(funnel), Write(num_receiver), Write(num_source), run_time=min(0.8, anim_duration*0.3))
                
                animations = []
                for dot in waterfall_dots:
                    target_y = funnel.get_top()[1] - 0.2
                    target_x = funnel.get_center()[0] + random.uniform(-funnel_top.width/2 *0.7, funnel_top.width/2 *0.7) 
                    path = Line(dot.get_center(), [target_x, target_y - 3, 0]) 
                    if abs(dot.get_center()[0] - funnel.get_center()[0]) > funnel_top.width/2 * 1.5: 
                        path = Line(dot.get_center(), dot.get_center() + DOWN*4 + RIGHT*random.uniform(-1,1))
                    animations.append(MoveAlongPath(dot, path, rate_func=linear, run_time=random.uniform(1.5, 2.5)))
                self.play(LaggedStart(*animations, lag_ratio=0.01), run_time=min(2.5, anim_duration*0.7))

            elif item["id"] == 3:
                one = Tex("1").scale(1.5).move_to(LEFT*3 + UP)
                zeros_group = VGroup().shift(UP)
                active_visuals.add(one, zeros_group)
                self.play(Write(one), run_time=min(0.5, anim_duration*0.2))
                
                current_pos = one.get_right() + RIGHT*0.2
                for i in range(10): 
                    zero = Tex("0").scale(1.5).move_to(current_pos)
                    zeros_group.add(zero)
                    self.play(Write(zero), run_time=min(0.15, anim_duration*0.07))
                    current_pos = zero.get_right() + RIGHT*0.2
                    if current_pos[0] > config.frame_width/2 - 1: break
                if anim_duration > (0.5 + 10*0.15) : self.wait(anim_duration - (0.5 + 10*0.15))

            elif item["id"] == 4:
                stream_group = VGroup().shift(UP*0.5)
                for i in range(4): 
                    num_stream_str = "".join([str(random.randint(0,9)) for _ in range(30)])
                    stream_text = Text(num_stream_str, font="Monospace", font_size=20)
                    stream_text.move_to(LEFT*config.frame_width/2 + UP*(1.5-i*0.7))
                    stream_group.add(stream_text)
                
                speed_text = Tex("300 Gbps", color=YELLOW).scale(0.8).to_corner(UR)
                active_visuals.add(stream_group, speed_text)
                self.play(Write(speed_text), Create(stream_group), run_time=min(0.5, anim_duration*0.3))
                self.play(stream_group.animate.shift(RIGHT*config.frame_width*1.2).set_opacity(0), 
                          run_time=min(1.5, anim_duration*0.7), rate_func=linear)

            elif item["id"] == 5:
                bar = Rectangle(width=5, height=0.3, color=GRAY).shift(UP)
                fill = Rectangle(width=0.01, height=0.3, color=GREEN, fill_opacity=0.7).align_to(bar, LEFT)
                label = MathTex(r"0\%").next_to(bar, DOWN)
                
                def label_updater_for_id5(mob_to_update):
                    current_bar_width = bar.width
                    current_fill_width = fill.width
                    percent_val_str = r"0\%" 

                    if current_bar_width is None or current_fill_width is None:
                        percent_val_str = r"Err\%"
                    elif abs(current_bar_width) < 1e-9: 
                        percent_val_str = r"N/A\%"
                    else:
                        percent_val = (current_fill_width / current_bar_width) * 100
                        if np.isnan(percent_val) or np.isinf(percent_val):
                            percent_val_str = r"CalcErr\%"
                        else:
                            percent_val_str = f"{int(np.clip(percent_val, 0, 1000))}\%"
                    mob_to_update.become(MathTex(percent_val_str).next_to(bar,DOWN))

                label.add_updater(label_updater_for_id5)
                
                active_visuals.add(bar, fill, label)
                self.play(Create(bar), Create(fill), Write(label), run_time=min(0.7, anim_duration*0.3))
                
                original_fill_height = fill.height
                self.play(
                    fill.animate.set_width(bar.width * 0.95) 
                          .set_height(original_fill_height)
                          .align_to(bar, LEFT),
                    run_time=min(1.2, anim_duration*0.5)
                )
                self.play(fill.animate.shift(RIGHT*0.05), bar.animate.shift(RIGHT*0.05), label.animate.shift(RIGHT*0.05), run_time=0.05)
                self.play(fill.animate.shift(LEFT*0.1), bar.animate.shift(LEFT*0.1), label.animate.shift(LEFT*0.1), run_time=0.05)
                self.play(fill.animate.shift(RIGHT*0.05), bar.animate.shift(RIGHT*0.05), label.animate.shift(RIGHT*0.05), run_time=0.05)
                if anim_duration > 2.05 : self.wait(anim_duration - 2.05)


            elif item["id"] == 6:
                container = Rectangle(width=2, height=3, color=WHITE).shift(UP*0.5)
                water_level_tracker = ValueTracker(0.01) 
                water = always_redraw(lambda:
                    Rectangle(width=1.98, height=max(0.01, min(container.height * 1.25, container.height * water_level_tracker.get_value())), 
                              color=BLUE_D, fill_opacity=0.6)
                    .align_to(container, DOWN)
                    .align_to(container, LEFT) # Corrected alignment
                )
                capacity_text_obj = DecimalNumber(0, unit=r"\%").scale(0.8)
                capacity_text_obj.next_to(container, RIGHT)

                def capacity_updater_id6(mob):
                    val = water_level_tracker.get_value() * 100
                    if np.isnan(val) or np.isinf(val):
                        mob.set_value(0)
                    else:
                        mob.set_value(np.clip(val, 0, 125))
                    mob.next_to(container, RIGHT)

                capacity_text_obj.add_updater(capacity_updater_id6)
                
                active_visuals.add(container, water, capacity_text_obj)
                self.play(Create(container), Create(water), Write(capacity_text_obj), run_time=min(0.8, anim_duration*0.25))
                self.play(water_level_tracker.animate.set_value(1.2), run_time=min(1.5, anim_duration*0.4)) 
                
                choked_text = Tex("呛住!", color=RED).move_to(container.get_center() + UP*container.height*0.2)
                new_capacity_display = Tex("0 Breath", color=RED).scale(0.7).move_to(capacity_text_obj.get_center())
                active_visuals.add(choked_text) # Add before ReplacementTransform needs it as a target

                self.play(
                    water_level_tracker.animate.set_value(0.9), 
                    container.animate.set_fill(RED, opacity=0.3), 
                    ReplacementTransform(capacity_text_obj, new_capacity_display), # USE REPLACEMENTTRANSFORM
                    Write(choked_text),
                    run_time=min(1.2, anim_duration*0.35)
                )
                active_visuals.remove(capacity_text_obj).add(new_capacity_display) # Update active visuals


            elif item["id"] == 7:
                target_text = Tex("接收目标:", font_size=30).shift(UP*1.5)
                old_goal = MathTex(r"100\%", color=RED).next_to(target_text, DOWN)
                arrow = Arrow(old_goal.get_right() + RIGHT*0.3, old_goal.get_right() + RIGHT*1.3, buff=0.1, color=YELLOW)
                new_goal_text = MathTex(r"0\%", color=GREEN).next_to(arrow, RIGHT)
                
                active_visuals.add(target_text, old_goal, arrow, new_goal_text)
                self.play(Write(target_text), Write(old_goal), run_time=min(0.8, anim_duration*0.4))
                self.play(
                    GrowArrow(arrow), 
                    ReplacementTransform(old_goal, new_goal_text.copy().move_to(old_goal.get_center())), # USE REPLACEMENTTRANSFORM
                    Write(new_goal_text), # Write the one at the final position
                    run_time=min(1.0, anim_duration*0.6)
                )
            
            elif item["id"] == 8:
                pipe_in = Rectangle(width=2, height=0.5, color=GRAY, fill_opacity=0.5).shift(LEFT*1.5 + UP)
                pipe_out = Rectangle(width=2, height=0.5, color=GRAY, fill_opacity=0.5).shift(RIGHT*1.5+ UP)
                valve_body = Circle(radius=0.4, color=DARK_GRAY, fill_opacity=0.8).shift(UP)
                valve_handle = Line(UP*0.4, DOWN*0.4, color=RED, stroke_width=6).rotate(-PI/4).move_to(valve_body.get_center())
                
                flow_rate_text = Tex("流量: ", font_size=28).next_to(valve_body, DOWN, buff=0.5)
                flow_value = DecimalNumber(70, unit=r"\%", font_size=28).next_to(flow_rate_text, RIGHT, buff=0.1)
                
                active_visuals.add(pipe_in, pipe_out, valve_body, valve_handle, flow_rate_text, flow_value)
                self.play(
                    Create(pipe_in), Create(pipe_out), Create(valve_body), Create(valve_handle),
                    Write(flow_rate_text), Write(flow_value),
                    run_time=min(1.2, anim_duration*0.4)
                )
                self.play(Rotate(valve_handle, angle=PI/2, about_point=valve_body.get_center()),
                          flow_value.animate.set_value(0),
                          run_time=min(0.8, anim_duration*0.3))
                self.play(Rotate(valve_handle, angle=-PI/3, about_point=valve_body.get_center()), 
                          flow_value.animate.set_value(50),
                          run_time=min(0.8, anim_duration*0.3))

            elif item["id"] == 9:
                title_text_1 = Text("《Liya的智慧锦囊》", font_size=28).shift(UP*2.2)
                title_text_2 = Text("今天送你三个“认知止水阀”", font_size=28).next_to(title_text_1, DOWN*1.2)
                
                valve_icon_1 = self.create_valve_icon().shift(LEFT*2.5 + UP*0.2)
                valve_icon_2 = self.create_valve_icon().shift(UP*0.2)
                valve_icon_3 = self.create_valve_icon().shift(RIGHT*2.5+ UP*0.2)
                num_1 = MathTex("1").next_to(valve_icon_1, DOWN)
                num_2 = MathTex("2").next_to(valve_icon_2, DOWN)
                num_3 = MathTex("3").next_to(valve_icon_3, DOWN)

                self.valve_icons = VGroup(valve_icon_1, valve_icon_2, valve_icon_3)
                self.valve_nums = VGroup(num_1,num_2,num_3)
                active_visuals.add(title_text_1, title_text_2, self.valve_icons, self.valve_nums)
                self.play(Write(title_text_1), Write(title_text_2), run_time=min(1.5, anim_duration*0.3))
                self.play(LaggedStart(
                    FadeIn(valve_icon_1, scale=0.5), Write(num_1),
                    FadeIn(valve_icon_2, scale=0.5), Write(num_2),
                    FadeIn(valve_icon_3, scale=0.5), Write(num_3),
                    lag_ratio=0.3,
                    run_time=min(2.5, anim_duration*0.7)
                ))
            
            elif item["id"] == 10:
                if self.valve_icons and self.valve_nums and len(self.valve_icons) > 0: 
                    active_visuals.add(self.valve_icons, self.valve_nums) 
                    self.play(self.valve_icons[0].animate.set_color(YELLOW).scale(1.2),
                              self.valve_nums[0].animate.set_color(YELLOW).scale(1.2),
                              run_time=min(0.8, anim_duration*0.5))
                    self.valve_icons[0].scale_factor = 1.2 # Store current scale for reset
                    self.valve_nums[0].scale_factor = 1.2
                    if len(self.valve_icons) > 1:
                        self.play(self.valve_icons[1:].animate.set_opacity(0.4),
                                  self.valve_nums[1:].animate.set_opacity(0.4),
                                  run_time=min(0.5, anim_duration*0.5))
                else: 
                    placeholder = Tex("阀门1: 开局过滤").shift(UP)
                    active_visuals.add(placeholder)
                    self.play(Write(placeholder), run_time=anim_duration)

            elif item["id"] == 11:
                phone_rect = Rectangle(width=0.8, height=1.5, color=LIGHT_GRAY, fill_opacity=0.8).round_corners(0.1)
                phone_screen = Rectangle(width=0.7, height=1.3, color=BLACK, fill_opacity=1).move_to(phone_rect)
                phone_icon = VGroup(phone_rect, phone_screen).scale(0.8).shift(UP*0.5 + LEFT*1.5)
                timer_text_0 = MathTex(r"0\text{s}", color=RED).scale(0.8).next_to(phone_icon, RIGHT, buff=0.2)
                cross_mark = Cross(phone_icon, stroke_color=RED, stroke_width=6)
                brain_shape = Ellipse(width=1.2, height=0.8, color=PINK, fill_opacity=0.5).shift(UP*0.5 + RIGHT*1.5)
                brain_line1 = Line(brain_shape.get_left() + RIGHT*0.2, brain_shape.get_right() - RIGHT*0.2, stroke_color=PINK, stroke_width=2).rotate(PI/8).move_to(brain_shape)
                brain_line2 = Line(brain_shape.get_top() + DOWN*0.1, brain_shape.get_bottom() + UP*0.1, stroke_color=PINK, stroke_width=2).rotate(-PI/6).move_to(brain_shape)
                brain_icon = VGroup(brain_shape, brain_line1, brain_line2)
                buffer_text = MathTex(r">0\text{s Buffer}", color=GREEN).scale(0.7).next_to(brain_icon, RIGHT, buff=0.2)
                
                active_visuals.add(phone_icon, timer_text_0, brain_icon, buffer_text)
                self.play(FadeIn(phone_icon), Write(timer_text_0), run_time=min(0.7, anim_duration*0.3))
                self.play(Create(cross_mark.move_to(phone_icon)), run_time=min(0.5, anim_duration*0.2))
                active_visuals.add(cross_mark)
                self.play(FadeIn(brain_icon), Write(buffer_text), run_time=min(0.7, anim_duration*0.5))

            elif item["id"] == 12:
                plate = Circle(radius=0.8, color=WHITE, fill_opacity=0.2, stroke_width=2).shift(UP*0.5)
                info_morsel = Star(n=5, outer_radius=0.3, inner_radius=0.15, color=GOLD, fill_opacity=0.8).move_to(plate)
                num_one = MathTex(r"1^{\text{st}}").scale(0.7).next_to(plate, UP, buff=0.1)
                first_info_text = Tex("第一口信息", font_size=24).next_to(plate, DOWN)

                active_visuals.add(plate, info_morsel, num_one, first_info_text)
                self.play(Create(plate), FadeIn(info_morsel, scale=0.5), Write(num_one), Write(first_info_text), run_time=min(1.0, anim_duration))

            elif item["id"] == 13:
                baseline = Line(LEFT*3.5, RIGHT*3.5, color=BLUE_A, stroke_width=5).shift(UP*0.5)
                label_baseline = Tex("认知基调", font_size=28).next_to(baseline, UP, buff=0.2)
                purity_text = MathTex(r"100\% \text{ 纯度}", color=GREEN).scale(0.9).next_to(baseline, DOWN, buff=0.2)
                glass_bottom = Line(LEFT*0.5, RIGHT*0.5)
                glass_left = Line(LEFT*0.5, LEFT*0.6 + UP*1.5)
                glass_right = Line(RIGHT*0.5, RIGHT*0.6 + UP*1.5)
                glass_top_opening = ArcBetweenPoints(glass_left.get_end(), glass_right.get_end(), angle=-PI*0.8)
                glass = VGroup(glass_bottom, glass_left, glass_right, glass_top_opening).scale(0.8).next_to(purity_text, RIGHT, buff=0.5)
                water_in_glass = Polygon(
                    glass_bottom.get_start(), glass_bottom.get_end(),
                    glass_right.get_start() + UP*(glass_right.get_length()*0.9), 
                    glass_left.get_start() + UP*(glass_left.get_length()*0.9),
                    color=BLUE_B, fill_opacity=0.6
                ).move_to(glass.get_center()+DOWN*0.05)

                active_visuals.add(baseline, label_baseline, purity_text, glass, water_in_glass)
                self.play(Create(baseline), Write(label_baseline), Write(purity_text), run_time=min(1.2, anim_duration*0.5))
                self.play(Create(glass), FadeIn(water_in_glass), run_time=min(1.0, anim_duration*0.5))
            
            elif item["id"] == 14:
                clock_face = Circle(radius=1, color=GRAY).shift(UP*0.5)
                center_dot = Dot(clock_face.get_center(), color=WHITE)
                minute_hand = Line(center_dot.get_center(), center_dot.get_center() + UP*0.8, color=WHITE, stroke_width=4)
                highlight_arc = Arc(radius=1, start_angle=PI/2, angle=-PI/3, color=GOLD, fill_opacity=0.5, stroke_width=0).move_to(clock_face.get_center())
                ten_min_text = MathTex(r"10 \text{ min}", color=GOLD).scale(0.8).next_to(clock_face, RIGHT, buff=0.3)
                golden_text = Tex("黄金", font_size=20, color=GOLD).next_to(ten_min_text, UP, buff=0.05)
                
                active_visuals.add(clock_face, center_dot, minute_hand, highlight_arc, ten_min_text, golden_text)
                self.play(Create(clock_face), Create(center_dot), GrowFromCenter(minute_hand), run_time=min(0.8, anim_duration*0.4))
                self.play(FadeIn(highlight_arc), Write(ten_min_text), Write(golden_text), run_time=min(1.0, anim_duration*0.6))

            elif item["id"] == 15:
                person_placeholder = Circle(radius=0.3, color=BLUE_D, fill_opacity=0.6).shift(UP*0.5) 
                passive_arrow = Arrow(LEFT*2.5, person_placeholder.get_left(), buff=0.1, color=RED_C, stroke_width=5)
                passive_text = MathTex(r"0\% \text{ 被动}", color=RED_C, font_size=28).next_to(passive_arrow, UP, buff=0.1)
                active_arrow = Arrow(person_placeholder.get_right(), RIGHT*2.5, buff=0.1, color=GREEN_C, stroke_width=5, tip_length=0.25)
                active_text = MathTex(r"100\% \text{ 主动}", color=GREEN_C, font_size=28).next_to(active_arrow, UP, buff=0.1)

                active_visuals.add(person_placeholder, passive_arrow, passive_text, active_arrow, active_text)
                self.play(Create(person_placeholder), run_time=min(0.3, anim_duration*0.1))
                self.play(GrowArrow(passive_arrow), Write(passive_text),
                          GrowArrow(active_arrow), Write(active_text),
                          run_time=min(1.5, anim_duration*0.7))
                self.play(passive_arrow.animate.set_opacity(0.3), passive_text.animate.set_opacity(0.3), run_time=min(0.5, anim_duration*0.2))

            elif item["id"] == 16:
                book_cover = Rectangle(width=0.8, height=1, color=BLUE_E, fill_opacity=0.7).shift(LEFT*2.5 + UP*0.5)
                book_pages = VGroup(*[Line(book_cover.get_bottom() + RIGHT*0.05*i + UP*0.02, book_cover.get_top() + RIGHT*0.05*i - UP*0.02, stroke_width=1.5, color=LIGHT_GRAY) for i in range(1,4)])
                book = VGroup(book_cover, book_pages)
                num_1_book = MathTex("1").scale(0.7).next_to(book, DOWN)
                book_text = Tex("书", font_size=20).next_to(num_1_book, DOWN, buff=0.05)
                bulb_glass = Circle(radius=0.4, color=YELLOW_A, fill_opacity=0.3).shift(UP*0.7) # Position bulb glass first
                bulb_base = Rectangle(width=0.3, height=0.2, color=GRAY).next_to(bulb_glass, DOWN, buff=0)
                bulb_lines = VGroup() 
                bulb_lines.add(Line(bulb_base.get_top()+LEFT*0.05, bulb_glass.get_center()+UP*0.1, stroke_color=YELLOW_D, stroke_width=1.5))
                bulb_lines.add(Line(bulb_base.get_top()+RIGHT*0.05, bulb_glass.get_center()+UP*0.1, stroke_color=YELLOW_D, stroke_width=1.5))
                lightbulb = VGroup(bulb_glass, bulb_base, bulb_lines) # Group them
                lightbulb.shift(UP*0.5) # Shift the entire assembled lightbulb
                num_1_idea = MathTex("1").scale(0.7).next_to(lightbulb, DOWN)
                idea_text = Tex("理念", font_size=20).next_to(num_1_idea, DOWN, buff=0.05)
                target_c1 = Circle(radius=0.5, color=RED_D, fill_opacity=0.8).shift(RIGHT*2.5 + UP*0.5)
                target_c2 = Circle(radius=0.3, color=WHITE, fill_opacity=0.9).move_to(target_c1)
                target_c3 = Circle(radius=0.1, color=RED_D, fill_opacity=1.0).move_to(target_c1)
                target = VGroup(target_c1,target_c2,target_c3)
                num_1_goal = MathTex("1").scale(0.7).next_to(target, DOWN)
                goal_text = Tex("目标", font_size=20).next_to(num_1_goal, DOWN, buff=0.05)
                
                active_visuals.add(book, num_1_book, book_text, lightbulb, num_1_idea, idea_text, target, num_1_goal, goal_text)
                self.play(
                    LaggedStart(
                        FadeIn(book, scale=0.7), Write(num_1_book), Write(book_text),
                        FadeIn(lightbulb, scale=0.7), Write(num_1_idea), Write(idea_text),
                        FadeIn(target, scale=0.7), Write(num_1_goal), Write(goal_text),
                        lag_ratio=0.4, run_time=min(2.5, anim_duration)
                    )
                )
            
            elif item["id"] == 17: # Valve highlighting logic
                if self.valve_icons and self.valve_nums and len(self.valve_icons) >= 2:
                    active_visuals.add(self.valve_icons, self.valve_nums)
                    animations_reset = []
                    for i in range(len(self.valve_icons)):
                        icon_scale = getattr(self.valve_icons[i], 'scale_factor', 1.0)
                        num_scale = getattr(self.valve_nums[i], 'scale_factor', 1.0)
                        animations_reset.append(self.valve_icons[i].animate.set_color(WHITE).scale(1.0/icon_scale if icon_scale != 0 else 1.0).set_opacity(1.0))
                        animations_reset.append(self.valve_nums[i].animate.set_color(WHITE).scale(1.0/num_scale if num_scale != 0 else 1.0).set_opacity(1.0))
                        self.valve_icons[i].scale_factor = 1.0 # Reset stored scale
                        self.valve_nums[i].scale_factor = 1.0
                    if animations_reset:
                        self.play(*animations_reset, run_time=min(0.3, anim_duration*0.1))
                        anim_duration = max(0.1, anim_duration - min(0.3, anim_duration*0.1))

                    self.play(self.valve_icons[1].animate.set_color(YELLOW).scale(1.2),
                              self.valve_nums[1].animate.set_color(YELLOW).scale(1.2),
                              run_time=min(0.8, anim_duration*0.5))
                    self.valve_icons[1].scale_factor = 1.2 
                    self.valve_nums[1].scale_factor = 1.2

                    other_indices = [i for i in [0, 2] if i < len(self.valve_icons) and i != 1]
                    other_icons = VGroup(*[self.valve_icons[i] for i in other_indices])
                    other_nums = VGroup(*[self.valve_nums[i] for i in other_indices])
                    if other_icons: # Check if group is not empty
                        self.play(other_icons.animate.set_opacity(0.4),
                                  other_nums.animate.set_opacity(0.4),
                                  run_time=min(0.5, anim_duration*0.4))
                else:
                    placeholder = Tex("阀门2: 主题感知锚").shift(UP)
                    active_visuals.add(placeholder)
                    self.play(Write(placeholder), run_time=anim_duration)

            elif item["id"] == 18:
                compass_rose = Star(n=8, outer_radius=0.8, inner_radius=0.4, color=BLUE_GRAY, fill_opacity=0.5).shift(UP*0.5 + LEFT*1.5)
                compass_needle = Arrow(ORIGIN, UP*0.6, buff=0, color=RED_D, stroke_width=5, tip_length=0.15).move_to(compass_rose.get_center())
                compass = VGroup(compass_rose, compass_needle)
                keyword_box_outline = Rectangle(width=2.5, height=0.7, color=WHITE).shift(UP*0.5 + RIGHT*1.5)
                self.keyword_text_mobject = Tex("关键词?", font_size=24).move_to(keyword_box_outline) 
                num_one = MathTex("1").scale(0.9).next_to(keyword_box_outline, DOWN, buff=0.2)
                nav_text = Tex("核心导航点", font_size=20).next_to(num_one, DOWN, buff=0.1)

                active_visuals.add(compass, keyword_box_outline, self.keyword_text_mobject, num_one, nav_text)
                self.play(Create(compass_rose), GrowArrow(compass_needle), run_time=min(1.0, anim_duration*0.4))
                self.play(Create(keyword_box_outline), Write(self.keyword_text_mobject), Write(num_one), Write(nav_text), run_time=min(1.5, anim_duration*0.6))

            elif item["id"] == 19:
                magnifying_glass_circle = Circle(radius=0.5, color=LIGHT_BLUE, stroke_width=5).shift(UP*0.5 + LEFT*0.5)
                magnifying_glass_handle = Line(magnifying_glass_circle.get_center()+DR*0.4, magnifying_glass_circle.get_center()+DR*1.2, color=LIGHT_BLUE, stroke_width=5)
                magnifying_glass = VGroup(magnifying_glass_circle, magnifying_glass_handle)
                num_one = MathTex(r"1\text{x}").scale(0.8).next_to(magnifying_glass, RIGHT, buff=0.3)
                scan_text = Tex("快速匹配", font_size=24).next_to(num_one, DOWN, buff=0.1)
                info_dots = VGroup(*[Dot(radius=0.05, color=random_bright_color(), fill_opacity=0.7).shift(UP*0.5 + RIGHT*2 + random.uniform(-0.5,0.5)*RIGHT + random.uniform(-0.3,0.3)*UP) for _ in range(5)])

                active_visuals.add(magnifying_glass, num_one, scan_text, info_dots)
                self.play(Create(magnifying_glass), Write(num_one), Write(scan_text), run_time=min(1.0, anim_duration*0.5))
                self.play(magnifying_glass.animate.move_to(info_dots.get_center()+LEFT*0.3), LaggedStartMap(FadeIn, info_dots), run_time=min(1.0, anim_duration*0.5))

            elif item["id"] == 20:
                if self.keyword_text_mobject: 
                    keyword_display = self.keyword_text_mobject.copy().scale(0.8).to_edge(UP, buff=0.5) # Keep original self.keyword_text_mobject as is
                    active_visuals.add(keyword_display)
                    self.play(FadeIn(keyword_display, shift=DOWN*0.2), run_time=min(0.5, anim_duration*0.1))
                    anim_duration = max(0.1, anim_duration - min(0.5, anim_duration*0.1))
                
                info_item_rect = Rectangle(width=1.5, height=0.8, color=ORANGE, fill_opacity=0.5).shift(UP*0.5)
                info_text_placeholder = Tex("信息片段", font_size=20).move_to(info_item_rect)
                info_item = VGroup(info_item_rect, info_text_placeholder)
                question_mark = Tex("?", color=YELLOW).scale(1.5).next_to(info_item, RIGHT, buff=0.5)
                score_one = MathTex(r"\text{相关 } \checkmark (1)", color=GREEN).scale(0.8).shift(DOWN*1 + LEFT*1.5)
                score_zero = MathTex(r"\text{无关 } \times (0)", color=RED).scale(0.8).shift(DOWN*1 + RIGHT*1.5)

                active_visuals.add(info_item, question_mark, score_one, score_zero)
                self.play(Create(info_item), Write(question_mark), run_time=min(1.0, anim_duration*0.4))
                self.play(FadeIn(score_one, shift=UP*0.2), FadeIn(score_zero, shift=UP*0.2), run_time=min(1.5, anim_duration*0.5))
            
            elif item["id"] == 21:
                score_zero_focus = MathTex(r"\text{无关 } \times (0)", color=RED).scale(1.2).move_to(UP*0.5)
                active_visuals.add(score_zero_focus)
                self.play(Write(score_zero_focus), run_time=anim_duration)

            elif item["id"] == 22:
                info_item_to_slide = Rectangle(width=2, height=1, color=GRAY, fill_opacity=0.6).round_corners(0.1).shift(UP*0.5)
                info_text_slide = Tex("无关信息", font_size=20).move_to(info_item_to_slide)
                item_slide = VGroup(info_item_to_slide, info_text_slide)
                energy_bar_outline = Rectangle(width=3, height=0.3, color=WHITE).next_to(item_slide, DOWN, buff=0.5)
                energy_bar_fill = Rectangle(width=2.9, height=0.3, color=GREEN_A, fill_opacity=0.7).align_to(energy_bar_outline, LEFT)
                energy_text = MathTex(r"\text{能量消耗} \approx 0", color=GREEN_A).scale(0.7).next_to(energy_bar_outline, DOWN)

                active_visuals.add(item_slide, energy_bar_outline, energy_bar_fill, energy_text)
                self.play(FadeIn(item_slide), Create(energy_bar_outline), Create(energy_bar_fill), Write(energy_text), run_time=min(1.0, anim_duration*0.4))
                self.play(item_slide.animate.shift(RIGHT*(config.frame_width/2 + item_slide.width/2 + 0.2)), run_time=min(1.0, anim_duration*0.6), rate_func=rush_into)

            elif item["id"] == 23:
                keyword_focus_text = Tex("今日关键词: “专注”", font_size=30).shift(UP*1.5)
                new_keyword_display = Tex("专注", font_size=24) # Target for transform
                if self.keyword_text_mobject: 
                    new_keyword_display.move_to(self.keyword_text_mobject.get_center())
                    self.play(ReplacementTransform(self.keyword_text_mobject, new_keyword_display), # USE REPLACEMENTTRANSFORM
                              run_time=min(0.5, anim_duration*0.2))
                    self.keyword_text_mobject = new_keyword_display # Update the reference
                    active_visuals.add(self.keyword_text_mobject) 
                    anim_duration = max(0.1, anim_duration - min(0.5, anim_duration*0.2))
                
                badge_no1 = Circle(radius=0.4, color=GOLD, fill_opacity=0.8).next_to(keyword_focus_text, DOWN, buff=0.3)
                text_no1 = MathTex(r"\#1", color=BLACK).scale(0.7).move_to(badge_no1)
                badge = VGroup(badge_no1, text_no1)

                active_visuals.add(keyword_focus_text, badge)
                self.play(Write(keyword_focus_text), FadeIn(badge, scale=0.5), run_time=min(1.5, anim_duration))

            elif item["id"] == 24:
                gossip_bubble_poly = Polygon(LEFT*1+DOWN*0.5,ORIGIN,RIGHT*1+DOWN*0.5,RIGHT*0.8+UP*0.3,RIGHT*1.2+UP*0.7,RIGHT*0.3+UP*0.8,LEFT*0.5+UP*0.5,LEFT*0.8+UP*0.2,color=PINK,fill_opacity=0.6,stroke_color=PURPLE_A).shift(UP*0.5+LEFT*1.5).scale(1.2)
                gossip_text = Tex("八卦...", font_size=20).move_to(gossip_bubble_poly).shift(UP*0.1)
                gossip_icon = VGroup(gossip_bubble_poly, gossip_text)
                priority_arrow = Arrow(gossip_icon.get_bottom()+DOWN*0.2, gossip_icon.get_bottom()+DOWN*1.2, color=RED, buff=0.1, stroke_width=6)
                priority_value = MathTex("-100", color=RED).scale(1.2).next_to(priority_arrow, DOWN, buff=0.1)
                priority_label = Tex("优先级", font_size=20).next_to(priority_value, DOWN, buff=0.1)

                active_visuals.add(gossip_icon, priority_arrow, priority_value, priority_label)
                self.play(Create(gossip_icon), run_time=min(0.8, anim_duration*0.3))
                self.play(GrowArrow(priority_arrow), Write(priority_value), Write(priority_label), run_time=min(1.2, anim_duration*0.7))

            elif item["id"] == 25: # Valve highlighting logic
                if self.valve_icons and self.valve_nums and len(self.valve_icons) >= 3:
                    active_visuals.add(self.valve_icons, self.valve_nums)
                    animations_reset = []
                    for i in range(len(self.valve_icons)):
                        icon_scale = getattr(self.valve_icons[i], 'scale_factor', 1.0)
                        num_scale = getattr(self.valve_nums[i], 'scale_factor', 1.0)
                        animations_reset.append(self.valve_icons[i].animate.set_color(WHITE).scale(1.0/icon_scale if icon_scale != 0 else 1.0).set_opacity(1.0))
                        animations_reset.append(self.valve_nums[i].animate.set_color(WHITE).scale(1.0/num_scale if num_scale != 0 else 1.0).set_opacity(1.0))
                        self.valve_icons[i].scale_factor = 1.0
                        self.valve_nums[i].scale_factor = 1.0
                    if animations_reset:
                        self.play(*animations_reset, run_time=min(0.3, anim_duration*0.1))
                        anim_duration = max(0.1, anim_duration - min(0.3, anim_duration*0.1))
                        
                    self.play(self.valve_icons[2].animate.set_color(YELLOW).scale(1.2),
                              self.valve_nums[2].animate.set_color(YELLOW).scale(1.2),
                              run_time=min(0.8, anim_duration*0.5))
                    self.valve_icons[2].scale_factor = 1.2
                    self.valve_nums[2].scale_factor = 1.2
                    
                    other_indices = [i for i in [0, 1] if i < len(self.valve_icons) and i != 2]
                    other_icons = VGroup(*[self.valve_icons[i] for i in other_indices])
                    other_nums = VGroup(*[self.valve_nums[i] for i in other_indices])
                    if other_icons: # Check if group is not empty
                        self.play(other_icons.animate.set_opacity(0.4),
                                  other_nums.animate.set_opacity(0.4),
                                  run_time=min(0.5, anim_duration*0.4))
                else:
                    placeholder = Tex("阀门3: 睡前清理池").shift(UP)
                    active_visuals.add(placeholder)
                    self.play(Write(placeholder), run_time=anim_duration)
                
                soap_bar = Rectangle(width=0.8, height=0.5, color=LIGHT_SKY_BLUE, fill_opacity=0.7).round_corners(0.1)
                bubbles = VGroup(*[Circle(radius=random.uniform(0.05,0.1), color=WHITE,fill_opacity=0.5).shift(random.uniform(-0.2,0.2)*RIGHT + random.uniform(0.1,0.3)*UP) for _ in range(3)])
                valve_to_align_to = ORIGIN
                if self.valve_icons and len(self.valve_icons)>=3: valve_to_align_to = self.valve_icons[2]
                clean_icon = VGroup(soap_bar, bubbles).next_to(valve_to_align_to, RIGHT, buff=0.3).shift(UP*0.1)
                active_visuals.add(clean_icon)
                self.play(FadeIn(clean_icon, scale=0.5), run_time=min(0.5, anim_duration*0.1 if anim_duration > 0 else 0.1))


            elif item["id"] == 26:
                long_list = VGroup()
                for i in range(5):
                    list_item_box = Rectangle(width=3, height=0.4, color=GRAY, stroke_width=1)
                    list_item_text = Tex(f"信息条目 {i+1}", font_size=18)
                    checkbox = Square(side_length=0.2, color=WHITE, stroke_width=2).align_to(list_item_box, LEFT).shift(RIGHT*0.2)
                    list_item = VGroup(list_item_box, list_item_text.move_to(list_item_box), checkbox).shift(UP*(1.5 - i*0.5))
                    long_list.add(list_item)
                progress_text = Tex("阅读完成率:", font_size=24).next_to(long_list, DOWN, buff=0.3)
                progress_value = MathTex(r"70\% (\text{非 } 100\%)", color=YELLOW).next_to(progress_text, RIGHT)
                active_visuals.add(long_list, progress_text, progress_value)
                self.play(Create(long_list), Write(progress_text), Write(progress_value), run_time=anim_duration)

            elif item["id"] == 27:
                brain_icon_dirty = Ellipse(width=1.5, height=1, color=PINK, fill_opacity=0.3).shift(UP*0.5)
                cache_dots = VGroup(*[Dot(radius=random.uniform(0.02, 0.05), color=random_color(), fill_opacity=0.7)
                                      .move_to(brain_icon_dirty.get_center() + random.uniform(-0.6,0.6)*RIGHT + random.uniform(-0.3,0.3)*UP) 
                                      for _ in range(30)])
                cache_size_text = Tex("大脑缓存: ", font_size=24).next_to(brain_icon_dirty, DOWN)
                cache_value_dirty = MathTex(r"572\text{KB}", color=ORANGE).next_to(cache_size_text, RIGHT)
                cache_value_clean = MathTex(r"0\text{KB}", color=GREEN).move_to(cache_value_dirty.get_center()) # Target for transform
                active_visuals.add(brain_icon_dirty, cache_dots, cache_size_text, cache_value_dirty)
                self.play(Create(brain_icon_dirty), Create(cache_dots), Write(cache_size_text), Write(cache_value_dirty), run_time=min(1.5, anim_duration*0.4))
                
                wiper_stick = Line(UP*0.5, DOWN*0.5, color=BROWN, stroke_width=4)
                wiper_head = Rectangle(width=0.8, height=0.2, color=GRAY, fill_opacity=0.7).next_to(wiper_stick, DOWN, buff=0)
                wiper = VGroup(wiper_stick, wiper_head).move_to(brain_icon_dirty.get_center()+LEFT*1.5+UP*0.3).rotate(PI/6)
                active_visuals.add(wiper)

                self.play(FadeIn(wiper), run_time=min(0.5, anim_duration*0.1))
                self.play(
                    wiper.animate.move_to(brain_icon_dirty.get_center()+RIGHT*0.5).rotate(-PI/3),
                    FadeOut(cache_dots, scale=0.5),
                    ReplacementTransform(cache_value_dirty, cache_value_clean), # USE REPLACEMENTTRANSFORM
                    brain_icon_dirty.animate.set_fill(LIGHT_PINK, opacity=0.5), 
                    run_time=min(1.5, anim_duration*0.5)
                )
                active_visuals.remove(cache_value_dirty).add(cache_value_clean) # Update active visuals
                self.play(FadeOut(wiper), run_time=min(0.3, anim_duration*0.05 if anim_duration > 0 else 0.05))


            elif item["id"] == 28:
                moon_icon_full = Circle(radius=0.6, color=LIGHT_YELLOW, fill_opacity=0.7)
                moon_cutout = Circle(radius=0.55, color=config.background_color, fill_opacity=1).move_to(moon_icon_full.get_center()+RIGHT*0.2+DOWN*0.1)
                crescent_moon = Cutout(moon_icon_full, moon_cutout, fill_opacity=0.7).shift(UP*0.5 + LEFT*1.5)
                timer_display = VGroup(Integer(5, color=GOLD).scale(1.5), MathTex(r"\text{min}", color=GOLD).scale(0.8)).arrange(RIGHT, buff=0.1).next_to(crescent_moon, RIGHT, buff=0.5)
                active_visuals.add(crescent_moon, timer_display)
                self.play(DrawBorderThenFill(crescent_moon), Write(timer_display), run_time=anim_duration)

            elif item["id"] == 29:
                info_blocks_unsorted = VGroup()
                texts = ["重要信息A", "次要信息B", "待办C", "无关D", "核心E"]
                colors = [GREEN_C, YELLOW_C, BLUE_C, GRAY, GREEN_E]
                for i in range(5):
                    block = Rectangle(width=1.8, height=0.6, color=colors[i], fill_opacity=0.6).round_corners(0.1)
                    text = Tex(texts[i], font_size=16).move_to(block)
                    info_blocks_unsorted.add(VGroup(block, text))
                info_blocks_unsorted.arrange_in_grid(rows=2, cols=3, buff=0.3).shift(UP*0.5).scale(0.9)
                active_visuals.add(info_blocks_unsorted)
                self.play(LaggedStartMap(FadeIn, info_blocks_unsorted, scale=0.8, lag_ratio=0.1), run_time=min(1.5, anim_duration*0.4))

                sorted_positions = [UP*1.5 + LEFT*2, UP*1.5, UP*1.5 + RIGHT*2, DOWN*0.2 + LEFT*1, DOWN*0.2 + RIGHT*1] 
                priority_labels = VGroup()
                animations_sort = []
                important_indices = [0, 4] 
                
                for i in range(len(info_blocks_unsorted)):
                    animations_sort.append(info_blocks_unsorted[i].animate.move_to(sorted_positions[i]))
                self.play(*animations_sort, run_time=min(1.5, anim_duration*0.4))
                
                label_fade_ins = []
                current_label_num = 1
                for i in range(len(info_blocks_unsorted)): # Iterate again to position labels on now-moved blocks
                    if i in important_indices:
                        label_circle = Circle(radius=0.15, color=YELLOW, fill_opacity=0.8)
                        label_num_text = MathTex(str(current_label_num), color=BLACK).scale(0.5).move_to(label_circle)
                        label = VGroup(label_circle, label_num_text).next_to(info_blocks_unsorted[i],UR, buff=-0.05)
                        priority_labels.add(label)
                        label_fade_ins.append(FadeIn(label))
                        current_label_num +=1
                if label_fade_ins: # Check if there are any labels to fade in
                    active_visuals.add(priority_labels) # Add before FadeIn if they are created here
                    self.play(*label_fade_ins, run_time=min(0.5, anim_duration*0.2))


            elif item["id"] == 30:
                keep_box = Rectangle(width=2.5, height=1.5, color=GREEN_D, fill_opacity=0.2).round_corners(0.1).shift(UP*0.5 + LEFT*2)
                keep_label = Tex("值得记 (+)", color=GREEN_D, font_size=24).next_to(keep_box, UP, buff=0.1)
                delete_bin_body = Polygon(LEFT*0.5+DOWN*0.7,RIGHT*0.5+DOWN*0.7,RIGHT*0.6+UP*0.7,LEFT*0.6+UP*0.7,color=RED_D,fill_opacity=0.2).shift(UP*0.5+RIGHT*2)
                delete_bin_lid = Line(delete_bin_body.get_corner(UL)+LEFT*0.1, delete_bin_body.get_corner(UR)+RIGHT*0.1, color=RED_D, stroke_width=3).next_to(delete_bin_body, UP, buff=0)
                delete_bin = VGroup(delete_bin_body, delete_bin_lid)
                delete_label = Tex("该删除 (-)", color=RED_D, font_size=24).next_to(delete_bin, UP, buff=0.1)
                active_visuals.add(keep_box, keep_label, delete_bin, delete_label)
                self.play(Create(keep_box), Write(keep_label), Create(delete_bin), Write(delete_label), run_time=min(1.5, anim_duration*0.5))
                info_to_sort_1 = Tex("重要结论", font_size=20).set_color(GREEN_B).shift(DOWN*1.5)
                info_to_sort_2 = Tex("无用杂念", font_size=20).set_color(RED_B).next_to(info_to_sort_1, RIGHT, buff=1)
                active_visuals.add(info_to_sort_1, info_to_sort_2)
                self.play(Write(info_to_sort_1), Write(info_to_sort_2), run_time=min(0.5, anim_duration*0.1))
                self.play(info_to_sort_1.animate.move_to(keep_box.get_center()),
                          info_to_sort_2.animate.move_to(delete_bin.get_center()),
                          run_time=min(1.0, anim_duration*0.4))
                self.play(FadeOut(info_to_sort_1), FadeOut(info_to_sort_2), run_time=0.2)

            elif item["id"] == 31:
                pie_chart_full = Circle(radius=1.2, color=DARK_GRAY, fill_opacity=0.7, stroke_width=0).shift(UP*0.5)
                cleanup_sector = Sector(outer_radius=1.2, start_angle=0, angle=0.02*PI, color=LIGHT_BLUE, fill_opacity=0.9, stroke_width=0).move_to(pie_chart_full.get_center()) 
                one_percent_text = MathTex(r"1\%", color=WHITE).scale(0.7).move_to(cleanup_sector.point_from_proportion(0.5)) 
                label_text = Tex("认知整理术", font_size=24).next_to(pie_chart_full, DOWN)
                active_visuals.add(pie_chart_full, cleanup_sector, one_percent_text, label_text)
                self.play(Create(pie_chart_full), run_time=min(0.7, anim_duration*0.3))
                self.play(Create(cleanup_sector), Write(one_percent_text), Write(label_text), run_time=min(1.5, anim_duration*0.7))

            elif item["id"] == 32:
                brain_icon = Ellipse(width=1.8, height=1.2, color=PINK, fill_opacity=0.4).shift(UP*0.5 + LEFT*1.5)
                mold_spots = VGroup(*[Dot(radius=random.uniform(0.03,0.07), color=DARKER_GREEN, fill_opacity=0.6).move_to(brain_icon.get_center() + RIGHT*random.uniform(-0.7,0.7) + UP*random.uniform(-0.4,0.4)) for _ in range(5)])
                mold_index_text = Tex("霉菌指数: ", font_size=24).next_to(brain_icon, RIGHT, buff=0.5).align_to(brain_icon, UP)
                mold_value = DecimalNumber(25, unit=r"\%", color=DARKER_GREEN).next_to(mold_index_text, RIGHT)
                active_visuals.add(brain_icon, mold_spots, mold_index_text, mold_value)
                self.play(Create(brain_icon), Create(mold_spots), Write(mold_index_text), Write(mold_value), run_time=min(1.5, anim_duration*0.4))
                self.play(FadeOut(mold_spots, scale=0.3),
                          brain_icon.animate.set_fill(LIGHT_PINK, opacity=0.6), 
                          mold_value.animate.set_value(0).set_color(GREEN),
                          run_time=min(2.0, anim_duration*0.6))
            
            elif item["id"] == 33:
                lightbulb_icon_glass = Circle(radius=0.4, color=YELLOW_A, fill_opacity=0.3).shift(UP*0.7 + LEFT*0.5)
                lightbulb_icon_base = Rectangle(width=0.3, height=0.2, color=GRAY).next_to(lightbulb_icon_glass, DOWN, buff=0)
                lightbulb_icon = VGroup(lightbulb_icon_glass, lightbulb_icon_base)
                num_one = MathTex("1").scale(1.2).next_to(lightbulb_icon, RIGHT, buff=0.3)
                tip_text = Tex("重要提醒", font_size=24).next_to(num_one, RIGHT, buff=0.2)
                active_visuals.add(lightbulb_icon, num_one, tip_text)
                self.play(lightbulb_icon_glass.animate.set_fill(YELLOW_D, opacity=0.8), Write(num_one), Write(tip_text), run_time=anim_duration)

            elif item["id"] == 34:
                waves = VGroup()
                num_wave_layers = 3
                for i in range(num_wave_layers):
                    wave_segment_path = lambda t, i_offset=i: np.array([ (t-0.5) * (config.frame_width + 1), 0.3 * np.sin( (t-0.5)*2*PI*2 + i_offset*PI/2 + PI*self.renderer.time), 0]) # Add self.renderer.time for animation
                    single_wave = ParametricFunction(wave_segment_path, t_range=np.array([0, 1]), fill_opacity=0)
                    wave_fill_points = single_wave.get_points()
                    wave_fill_points = np.append(wave_fill_points, [RIGHT*(config.frame_width/2 + 0.5) + DOWN*2], axis=0) 
                    wave_fill_points = np.append(wave_fill_points, [LEFT*(config.frame_width/2 + 0.5) + DOWN*2], axis=0) 
                    wave_vmobject = Polygon(*wave_fill_points, stroke_width=0, fill_color=BLUE_E, fill_opacity=0.4 - i*0.1)
                    wave_vmobject.shift(UP*(0.5 - i*0.4))
                    waves.add(wave_vmobject)
                # For animating waves, you'd typically add an updater to the waves or use AnimationGroup
                # For a static display within the subtitle duration:
                infinity_liters = MathTex(r"\infty \text{ Liters}", color=WHITE).scale(1.2).move_to(UP*1.5)
                active_visuals.add(waves, infinity_liters)
                self.play(LaggedStartMap(Create, waves, lag_ratio=0.2), Write(infinity_liters), run_time=anim_duration)

            elif item["id"] == 35:
                current_reception = VGroup(MathTex("100").scale(1.5), Tex("单位接收量", font_size=20)).arrange(DOWN).shift(UP*0.5 + LEFT*2)
                arrow_to_more = Arrow(current_reception.get_right(), current_reception.get_right() + RIGHT*1.5, buff=0.2, color=YELLOW)
                target_more = MathTex("1000", color=RED).scale(1.8).next_to(arrow_to_more, RIGHT)
                cross_on_target = Cross(target_more, stroke_color=RED, stroke_width=8)
                active_visuals.add(current_reception, arrow_to_more, target_more)
                self.play(Write(current_reception), GrowArrow(arrow_to_more), Write(target_more), run_time=min(1.5, anim_duration*0.7))
                self.play(Create(cross_on_target), run_time=min(0.5, anim_duration*0.3))
                active_visuals.add(cross_on_target)

            elif item["id"] == 36: # Stream transformation - can be complex for Transform
                num_visual_streams = 20 
                start_y_range = 2.5
                streams_disordered = VGroup()
                for i in range(num_visual_streams):
                    start_point = LEFT*(config.frame_width/2-1)+UP*random.uniform(-start_y_range,start_y_range)
                    mid_point1 = start_point+RIGHT*random.uniform(1,2)+UP*random.uniform(-0.5,0.5)
                    mid_point2 = mid_point1+RIGHT*random.uniform(1,2)+UP*random.uniform(-0.5,0.5)
                    end_point_disordered = start_point+RIGHT*(config.frame_width-2)+UP*random.uniform(-start_y_range/1.5,start_y_range/1.5)
                    stream = CubicBezier(start_point,mid_point1,mid_point2,end_point_disordered,stroke_color=random_bright_color(),stroke_width=1.5,stroke_opacity=0.7)
                    streams_disordered.add(stream)
                
                num_100_text = MathTex("100x",color=GRAY).next_to(streams_disordered,LEFT,buff=0.3).shift(UP*0.2)
                active_visuals.add(streams_disordered,num_100_text)
                self.play(Create(streams_disordered),Write(num_100_text),run_time=min(1.0,anim_duration*0.3))

                ordered_channel_center_y = UP*0.2
                ordered_channel_line = Line(LEFT*(config.frame_width/2-1)+ordered_channel_center_y,RIGHT*(config.frame_width/2-1)+ordered_channel_center_y,stroke_color=BLUE_A,stroke_width=10)
                num_1_text = MathTex("1x",color=BLUE_A).next_to(ordered_channel_line,LEFT,buff=0.3)
                
                # For Transform to work better, target_paths should be structured VMobjects.
                # Transforming Bezier curves to simple Lines can sometimes cause issues if point counts differ wildly.
                # A FadeOut/FadeIn might be more robust if Transform gives broadcasting errors here.
                # Let's try to make target_paths simple lines for now.
                target_lines_for_transform = VGroup()
                for _ in range(num_visual_streams):
                    # Create lines that roughly align with the main ordered channel
                    start_x = LEFT[0]*(config.frame_width/2-1) + random.uniform(0, 0.5)
                    end_x = RIGHT[0]*(config.frame_width/2-1) - random.uniform(0, 0.5)
                    line = Line(start_x*RIGHT + ordered_channel_center_y, end_x*RIGHT + ordered_channel_center_y, stroke_color=BLUE_A, stroke_width=2, stroke_opacity=0.6)
                    target_lines_for_transform.add(line)

                self.play(
                    LaggedStart(*[Transform(streams_disordered[i], target_lines_for_transform[i]) for i in range(num_visual_streams)], lag_ratio=0.05),
                    ReplacementTransform(num_100_text, num_1_text), # Use ReplacementTransform
                    run_time=min(1.8, anim_duration*0.6)
                )
                active_visuals.remove(streams_disordered).add(target_lines_for_transform) # Keep transformed lines
                active_visuals.remove(num_100_text).add(num_1_text) # Keep transformed text
                active_visuals.add(ordered_channel_line)
                self.play(Create(ordered_channel_line), run_time=min(0.2, anim_duration*0.1))

            # --- End of ID blocks ---
            
            time_already_spent_in_segment_anims = 0 # This would need to be calculated more accurately
            remaining_segment_time = duration - (text_appear_time + time_already_spent_in_segment_anims + (0.2 if item["id"] > 1 else 0))
            if remaining_segment_time > 0.01:
                 self.wait(remaining_segment_time)

            current_scene_time = end_time


        if active_visuals:
            self.play(FadeOut(active_visuals), run_time=0.5)
        if subtitle_mobj: 
            self.play(FadeOut(subtitle_mobj), run_time=0.5)
        self.wait(1)

    def create_valve_icon(self):
        valve_body = Circle(radius=0.25, color=GRAY, fill_opacity=0.7)
        valve_handle = Line(UP*0.25, DOWN*0.25, color=RED_D, stroke_width=4).rotate(-PI/4)
        valve_handle.move_to(valve_body.get_center())
        icon = VGroup(valve_body, valve_handle).scale(0.8)
        icon.scale_factor = 1.0  # Initialize scale_factor
        return icon
