from great_tables import GT, style, google_font, loc, px, pct

def dubois_table(df, *, title=None, subtitle=None, source_note=None, **kwargs):
    """
    Return a W.E.B. Du Bois-inspired formatted display table from a pandas DataFrame.

    Args:
        df: The data to display in the table.
        title: Main title displayed above the table.
        subtitle: Secondary title displayed below the main title.
        source_note: Attribution or source note displayed below the table.
        **kwargs: Additional formatting options passed to the underlying table renderer.

    Returns:
        A styled table object ready for presentation.
    """
    n_cols = len(df.columns)
    equal_col_width = pct(100 / n_cols)
    table_width = df.shape[1] * 135
    column_names_dict = {col: col.replace('_', ' ').title() for col in df.columns}

    formatted_table = (
        GT(df, **kwargs)
        .tab_options(
            table_background_color="#F5F2E1",
            table_font_size="13px",
            heading_background_color="aliceblue",
            table_width=px(table_width),
            table_layout="auto",
            column_labels_font_weight='bold',
            column_labels_text_transform="capitalize",
            table_body_hlines_color="darkgray"
        )
        .opt_table_font(font=[google_font(name="Baskervville SC"),
                              google_font(name="Libre Baskerville"),
                              "Baskerville", "Georgia", "Serif"])
        .cols_label(column_names_dict)
        .cols_width(cases={col: equal_col_width for col in df.columns})
    )

    # Add tab_header only if the user provides a title
    if title is not None:
        formatted_table = formatted_table.tab_header(title=title, subtitle=subtitle)

    # Add tab_source_note only if the user provides a source note
    if source_note is not None:
        formatted_table = formatted_table.tab_source_note(source_note=source_note)

    return formatted_table