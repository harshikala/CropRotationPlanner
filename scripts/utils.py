def clean_plot_name(plot_name):
    return plot_name.replace("(", "").replace(")", "").replace("'", "").replace(",", "").replace(" ", "_")
