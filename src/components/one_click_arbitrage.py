"""
一键套利执行功能组件
提供自动化套利交易执行、监控和分析功能
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import random
import time
import asyncio


class OneClickArbitrage:
    """一键套利执行器"""

    def __init__(self):
        self.exchanges = ["Binance", "OKX", "Huobi", "KuCoin", "Gate.io", "Bybit"]
        self.currencies = ["BTC", "ETH", "BNB", "ADA", "DOT", "LINK", "UNI", "MATIC"]

        # 初始化会话状态
        if "active_trades" not in st.session_state:
            st.session_state.active_trades = []
        if "trade_history" not in st.session_state:
            st.session_state.trade_history = []
        if "auto_execution_enabled" not in st.session_state:
            st.session_state.auto_execution_enabled = False

    def generate_arbitrage_opportunities(self):
        """生成当前套利机会"""
        opportunities = []

        for _ in range(random.randint(5, 15)):
            currency = random.choice(self.currencies)
            buy_exchange = random.choice(self.exchanges)
            sell_exchange = random.choice([ex for ex in self.exchanges if ex != buy_exchange])

            buy_price = random.uniform(20000, 50000) if currency == "BTC" else random.uniform(100, 5000)
            price_diff = random.uniform(0.1, 3.5)
            sell_price = buy_price * (1 + price_diff / 100)

            profit_potential = random.uniform(50, 2000)
            confidence = random.uniform(70, 95)
            estimated_duration = random.randint(30, 300)

            opportunities.append({
                "id": f"{currency}_{buy_exchange}_{sell_exchange}_{int(time.time())}",
                "currency": currency,
                "buy_exchange": buy_exchange,
                "sell_exchange": sell_exchange,
                "buy_price": buy_price,
                "sell_price": sell_price,
                "price_difference": price_diff,
                "profit_potential": profit_potential,
                "confidence": confidence,
                "estimated_duration": estimated_duration,
                "volume_available": random.uniform(1000, 10000),
                "risk_level": random.choice(["低", "中", "高"]),
                "liquidity": random.choice(["高", "中", "低"]),
                "created_at": datetime.now()
            })

        return pd.DataFrame(opportunities)

    def render_execution_settings(self):
        """渲染执行设置"""
        st.subheader("⚙️ 执行设置")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("**风险控制**")
            max_position_size = st.number_input(
                "最大仓位大小 ($)",
                min_value=100,
                max_value=100000,
                value=5000,
                step=100
            )

            max_price_diff = st.slider(
                "最大价格差 (%)",
                0.1, 5.0, 2.0, 0.1
            )

        with col2:
            st.markdown("**执行参数**")
            min_confidence = st.slider(
                "最低置信度 (%)",
                50, 95, 80, 5
            )

            max_execution_time = st.number_input(
                "最大执行时间 (秒)",
                min_value=10,
                max_value=300,
                value=60,
                step=10
            )

        with col3:
            st.markdown("**自动化设置**")
            auto_execution = st.checkbox(
                "启用自动执行",
                value=st.session_state.auto_execution_enabled
            )
            st.session_state.auto_execution_enabled = auto_execution

            if auto_execution:
                st.info("🤖 自动执行已启用")
            else:
                st.warning("⏸️ 手动执行模式")

        return {
            "max_position_size": max_position_size,
            "max_price_diff": max_price_diff,
            "min_confidence": min_confidence,
            "max_execution_time": max_execution_time,
            "auto_execution": auto_execution
        }

    def execute_arbitrage(self, opportunity, settings):
        """执行套利交易"""
        trade_id = f"trade_{int(time.time())}_{random.randint(1000, 9999)}"

        # 模拟交易执行
        execution_steps = [
            "验证市场数据",
            "检查账户余额",
            "下买单",
            "确认买单成交",
            "下卖单",
            "确认卖单成交",
            "计算实际利润"
        ]

        trade_data = {
            "id": trade_id,
            "opportunity_id": opportunity["id"],
            "currency": opportunity["currency"],
            "buy_exchange": opportunity["buy_exchange"],
            "sell_exchange": opportunity["sell_exchange"],
            "buy_price": opportunity["buy_price"],
            "sell_price": opportunity["sell_price"],
            "expected_profit": opportunity["profit_potential"],
            "position_size": min(settings["max_position_size"], opportunity["volume_available"]),
            "status": "executing",
            "steps_completed": [],
            "start_time": datetime.now(),
            "end_time": None,
            "actual_profit": 0,
            "fees_paid": 0,
            "slippage": 0
        }

        # 添加到活跃交易
        st.session_state.active_trades.append(trade_data)

        return trade_id

    def simulate_trade_execution(self, trade_id):
        """模拟交易执行过程"""
        # 找到交易
        trade = None
        for t in st.session_state.active_trades:
            if t["id"] == trade_id:
                trade = t
                break

        if not trade:
            return

        execution_steps = [
            "验证市场数据",
            "检查账户余额",
            "下买单",
            "确认买单成交",
            "下卖单",
            "确认卖单成交",
            "计算实际利润"
        ]

        # 模拟执行步骤
        for i, step in enumerate(execution_steps):
            time.sleep(0.5)  # 模拟执行时间
            trade["steps_completed"].append({
                "step": step,
                "timestamp": datetime.now(),
                "success": random.random() > 0.05  # 95%成功率
            })

            # 如果某步失败，停止执行
            if not trade["steps_completed"][-1]["success"]:
                trade["status"] = "failed"
                trade["end_time"] = datetime.now()
                break

        # 如果所有步骤成功
        if trade["status"] == "executing" and len(trade["steps_completed"]) == len(execution_steps):
            trade["status"] = "completed"
            trade["end_time"] = datetime.now()

            # 计算实际结果
            slippage = random.uniform(0, 0.5)  # 0-0.5%滑点
            fees = trade["position_size"] * 0.002  # 0.2%手续费

            trade["slippage"] = slippage
            trade["fees_paid"] = fees
            trade["actual_profit"] = trade["expected_profit"] * random.uniform(0.7, 0.95) - fees

            # 移动到历史记录
            st.session_state.trade_history.append(trade)
            st.session_state.active_trades.remove(trade)

    def render_opportunities_table(self, df, settings):
        """渲染套利机会表格"""
        st.subheader("🎯 当前套利机会")

        if df.empty:
            st.warning("暂无套利机会")
            return

        # 筛选符合条件的机会
        filtered_df = df[
            (df["price_difference"] <= settings["max_price_diff"]) &
            (df["confidence"] >= settings["min_confidence"])
        ].copy()

        if filtered_df.empty:
            st.warning("没有符合当前设置条件的套利机会")
            return

        # 格式化显示 - 使用向量化操作优化性能
        display_df = filtered_df.copy()
        # 向量化字符串格式化
        display_df["价格差"] = display_df["price_difference"].round(2).astype(str) + "%"
        display_df["预期利润"] = "$" + display_df["profit_potential"].round(0).astype(int).astype(str)
        display_df["置信度"] = display_df["confidence"].round(0).astype(int).astype(str) + "%"
        display_df["风险等级"] = display_df["risk_level"]
        display_df["流动性"] = display_df["liquidity"]

        # 显示表格 - 使用索引遍历替代iterrows()
        for i, idx in enumerate(display_df.index):
            row = display_df.iloc[i]
            with st.container():
                col1, col2, col3, col4, col5, col6 = st.columns([2, 2, 2, 2, 2, 1])

                with col1:
                    st.write(f"**{row['currency']}**")
                    st.write(f"{row['buy_exchange']} → {row['sell_exchange']}")

                with col2:
                    st.write(f"价格差: {row['价格差']}")
                    st.write(f"预期利润: {row['预期利润']}")

                with col3:
                    st.write(f"置信度: {row['置信度']}")
                    st.write(f"风险: {row['风险等级']}")

                with col4:
                    st.write(f"流动性: {row['流动性']}")
                    st.write(f"预计时长: {row['estimated_duration']}秒")

                with col5:
                    # 风险指示器
                    risk_color = {"低": "🟢", "中": "🟡", "高": "🔴"}[row["risk_level"]]
                    st.write(f"风险: {risk_color}")

                    # 推荐指示器
                    if row["confidence"] >= 85 and row["risk_level"] == "低":
                        st.write("🌟 **推荐**")
                    elif row["confidence"] >= 75:
                        st.write("👍 **良好**")
                    else:
                        st.write("⚠️ **谨慎**")

                with col6:
                    # 执行按钮
                    if st.button(
                        "⚡ 执行",
                        key=f"execute_{row['id']}",
                        type="primary" if row["confidence"] >= 85 else "secondary"
                    ):
                        trade_id = self.execute_arbitrage(filtered_df.iloc[idx], settings)
                        st.success(f"✅ 交易 {trade_id} 已启动")
                        st.rerun()

                st.markdown("---")

    def render_active_trades(self):
        """渲染活跃交易监控"""
        st.subheader("🔄 活跃交易监控")

        if not st.session_state.active_trades:
            st.info("当前没有活跃交易")
            return

        for trade in st.session_state.active_trades:
            with st.expander(f"交易 {trade['id']} - {trade['currency']} ({trade['status']})"):
                col1, col2 = st.columns(2)

                with col1:
                    st.write(f"**交易对:** {trade['currency']}")
                    st.write(f"**买入交易所:** {trade['buy_exchange']}")
                    st.write(f"**卖出交易所:** {trade['sell_exchange']}")
                    st.write(f"**仓位大小:** ${trade['position_size']:,.0f}")
                    st.write(f"**预期利润:** ${trade['expected_profit']:.0f}")

                with col2:
                    st.write(f"**状态:** {trade['status']}")
                    st.write(f"**开始时间:** {trade['start_time'].strftime('%H:%M:%S')}")

                    if trade['end_time']:
                        duration = (trade['end_time'] - trade['start_time']).total_seconds()
                        st.write(f"**执行时长:** {duration:.1f}秒")

                    # 进度条
                    progress = len(trade['steps_completed']) / 7
                    st.progress(progress)

                # 执行步骤
                st.write("**执行步骤:**")
                for step_data in trade['steps_completed']:
                    status_icon = "✅" if step_data['success'] else "❌"
                    st.write(f"{status_icon} {step_data['step']} - {step_data['timestamp'].strftime('%H:%M:%S')}")

    def render_trade_history(self):
        """渲染交易历史"""
        st.subheader("📈 交易历史")

        if not st.session_state.trade_history:
            st.info("暂无交易历史")
            return

        # 统计信息
        total_trades = len(st.session_state.trade_history)
        successful_trades = len([t for t in st.session_state.trade_history if t['status'] == 'completed'])
        total_profit = sum([t['actual_profit'] for t in st.session_state.trade_history if t['status'] == 'completed'])

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("总交易数", total_trades)

        with col2:
            success_rate = (successful_trades / total_trades * 100) if total_trades > 0 else 0
            st.metric("成功率", f"{success_rate:.1f}%")

        with col3:
            st.metric("总利润", f"${total_profit:.0f}")

        # 详细历史
        st.write("**详细记录:**")
        for trade in reversed(st.session_state.trade_history[-10:]):  # 显示最近10笔
            status_icon = "✅" if trade['status'] == 'completed' else "❌"
            profit_text = f"${trade['actual_profit']:.0f}" if trade['status'] == 'completed' else "失败"

            st.write(f"{status_icon} {trade['currency']} - {trade['buy_exchange']} → {trade['sell_exchange']} - {profit_text}")

    def render_post_trade_analysis(self):
        """渲染交易后分析"""
        st.subheader("📊 交易后分析")

        if not st.session_state.trade_history:
            st.info("暂无交易数据进行分析")
            return

        completed_trades = [t for t in st.session_state.trade_history if t['status'] == 'completed']

        if not completed_trades:
            st.info("暂无成功交易数据")
            return

        # 利润分析
        profits = [t['actual_profit'] for t in completed_trades]
        expected_profits = [t['expected_profit'] for t in completed_trades]

        col1, col2 = st.columns(2)

        with col1:
            # 预期vs实际利润对比
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=list(range(len(profits))),
                y=expected_profits,
                mode='lines+markers',
                name='预期利润',
                line=dict(color='blue')
            ))
            fig.add_trace(go.Scatter(
                x=list(range(len(profits))),
                y=profits,
                mode='lines+markers',
                name='实际利润',
                line=dict(color='green')
            ))
            fig.update_layout(
                title="预期 vs 实际利润",
                xaxis_title="交易序号",
                yaxis_title="利润 ($)"
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            # 滑点和手续费分析
            slippages = [t['slippage'] for t in completed_trades]
            fees = [t['fees_paid'] for t in completed_trades]

            fig = go.Figure()
            fig.add_trace(go.Bar(
                x=list(range(len(slippages))),
                y=slippages,
                name='滑点 (%)',
                yaxis='y'
            ))
            fig.add_trace(go.Bar(
                x=list(range(len(fees))),
                y=fees,
                name='手续费 ($)',
                yaxis='y2'
            ))
            fig.update_layout(
                title="滑点和手续费分析",
                xaxis_title="交易序号",
                yaxis=dict(title="滑点 (%)", side="left"),
                yaxis2=dict(title="手续费 ($)", side="right", overlaying="y")
            )
            st.plotly_chart(fig, use_container_width=True)


def render_one_click_arbitrage():
    """渲染一键套利执行主界面"""
    st.title("⚡ 一键套利执行系统")
    st.markdown("---")

    arbitrage = OneClickArbitrage()

    # 渲染执行设置
    settings = arbitrage.render_execution_settings()
    st.markdown("---")

    # 生成套利机会
    with st.spinner("扫描套利机会..."):
        opportunities_df = arbitrage.generate_arbitrage_opportunities()

    # 渲染机会表格
    arbitrage.render_opportunities_table(opportunities_df, settings)
    st.markdown("---")

    # 渲染活跃交易
    arbitrage.render_active_trades()
    st.markdown("---")

    # 渲染交易历史
    arbitrage.render_trade_history()
    st.markdown("---")

    # 渲染交易后分析
    arbitrage.render_post_trade_analysis()

    # 刷新按钮
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("🔄 刷新机会", key="arbitrage_refresh"):
            st.rerun()

    with col2:
        if st.button("🧹 清除历史", key="clear_history"):
            st.session_state.trade_history = []
            st.session_state.active_trades = []
            st.success("历史记录已清除")
            st.rerun()
