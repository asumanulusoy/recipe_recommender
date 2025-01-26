import pandas as pd
import plotly.express as px

def create_nutrition_comparison_chart(item1, item2, metrics):
    """
    Create a bar chart comparing nutritional values of two items
    
    Args:
        item1 (pd.Series): First item's data
        item2 (pd.Series): Second item's data
        metrics (list): List of nutritional metrics to compare
        
    Returns:
        plotly.graph_objects.Figure: Comparison chart
    """
    comparison_data = []
    
    for metric in metrics:
        comparison_data.extend([
            {'item': item1['item'], 'metric': metric, 'value': item1[metric]},
            {'item': item2['item'], 'metric': metric, 'value': item2[metric]}
        ])
    
    df_comparison = pd.DataFrame(comparison_data)
    
    fig = px.bar(
        df_comparison,
        x='metric',
        y='value',
        color='item',
        barmode='group',
        title='Nutritional Comparison'
    )
    
    return fig

def format_nutrition_info(item_data):
    """
    Format nutrition information for display
    
    Args:
        item_data (pd.Series): Item's nutritional data
        
    Returns:
        str: Formatted nutrition information
    """
    return f"""
    **Nutritional Information**
    - Calories: {item_data['calories']:.1f}
    - Total Fat: {item_data['total_fat']:.1f}g
    - Protein: {item_data['protein']:.1f}g
    - Carbs: {item_data['total_carb']:.1f}g
    - Fiber: {item_data['fiber']:.1f}g
    - Sugar: {item_data['sugar']:.1f}g
    """