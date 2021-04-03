def arrange_by_columns(entries, column_count):
    r = len(entries) % column_count
    if r > 0:
        entries.extend([None] * (column_count - r))
    entries_per_column = len(entries) // column_count

    columns = [
        entries[i * entries_per_column : (i + 1) * entries_per_column]
        for i in range(column_count)
    ]

    return zip(*columns)
