cmb_yt_settings = {
    'datasetName': 'Combined_comments',
    'dataSource': 'yt_comments',
    'corpusFieldName': 'comment_displayed',
    'dateFieldName': 'published_date',
    'json_orientation': 'columns',
    'roundToDay': False,
    # Advanced settings
    'numberTopics': 20,
    'numberWords': 10,
    'moving_average_size': 5,
    'reloadData': False,                # Will re-read your input file and train a new model with the updated data
    'retrainModel': False,              # Will use the currently saved data and train a new model (useful to try different settings without processing the same corpus)
    'minimumProbability': 0.00000001,
    'nbFigures': 10,
    'topicGroups': [[18, 15, 1, 7, 9, 5, 0, 8, 11, 3]],
    'addLegend': True,
}

covid_yt_settings = {
    'datasetName': 'COVID_March_YT_Comments',
    'dataSource': 'COVID_keywords_March_comments.json',
    'corpusFieldName': 'comment_displayed',
    'dateFieldName': 'published_date',
    'json_orientation': 'columns',
    'roundToDay': False,
    'model_type': 'LDA',
    'start_date': "2020-03-01",
    'end_date': "2020-04-01",
    # Advanced settings
    'numberTopics': 20,
    'numberWords': 10,
    'moving_average_size': 3,
    # 'moving_avg_window_size': 1000,
    'reloadData': False,                # Will re-read your input file and train a new model with the updated data
    'retrainModel': False,              # Will use the currently saved data and train a new model (useful to try different settings without processing the same corpus)
    'minimumProbability': 0.00000001,
    'distributionInWorksheet': False,
    'nbFigures': 0,
    'topicGroups': [[7, 17]],
    'addLegend': True,
}


covid_videos_settings = {
    'datasetName': 'COVID_March_videos',
    'dataSource': 'COVID_March_videos.json',
    'corpusFieldName': 'video_title',
    'dateFieldName': 'published_date',
    'json_orientation': 'columns',
    'roundToDay': False,
    'model_type': 'LDA',
    # Advanced settings
    'numberTopics': 20,
    'numberWords': 10,
    'moving_average_size': 15,
    # 'moving_avg_window_size': 1000,
    'reloadData': True,                # Will re-read your input file and train a new model with the updated data
    'retrainModel': True,              # Will use the currently saved data and train a new model (useful to try different settings without processing the same corpus)
    'minimumProbability': 0.00000001,
    'distributionInWorksheet': True,
    'nbFigures': 10,
    'topicGroups': [[0,17,6]],
    'addLegend': True
}

jan_yt_settings = {
    'datasetName': 'January_comments',
    'dataSource': 'January_2020.json',
    'corpusFieldName': 'comment_displayed',
    'dateFieldName': 'published_date',
    'json_orientation': 'columns',
    'roundToDay': False,
    'model_type': 'LDA',
    # Advanced settings
    'numberTopics': 20,
    'numberWords': 10,
    'moving_average_size': 1,
    # 'moving_avg_window_size': 1000,
    'reloadData': False,                # Will re-read your input file and train a new model with the updated data
    'retrainModel': True,              # Will use the currently saved data and train a new model (useful to try different settings without processing the same corpus)
    'minimumProbability': 0.00000001,
    'nbFigures': 10,
}

posts_settings = {
    'datasetName': 'vax_parler_5_greater_1',
    'dataSource': 'vax_parler_5_greater.csv',
    'corpusFieldName': 'body',
    'dateFieldName': 'created_at_formatted',
    'idFieldName': 'id',
    'json_orientation': 'records',
    'distributionInWorksheet': True,
    'roundToDay': False,
    # Advanced settings
    'numberTopics': 10,
    'numberWords': 10,
    'moving_average_size': 2,
    'reloadData': False,                # Will re-read your input file and train a new model with the updated data
    'retrainModel': False,              # Will use the currently saved data and train a new model (useful to try different settings without processing the same corpus)
    'minimumProbability': 0.00000001,
    'nbFigures': 10,
}

DOD_AUS_settings = {
    'datasetName': 'AUG',
    'dataSource': 'aug.json',
    'corpusFieldName': 'video_title',
    'dateFieldName': 'published_date',
    'json_orientation': 'records',
    'distributionInWorksheet': True,
    # Advanced settings
    'numberTopics': 5,
    'numberWords': 10,
    'moving_average_size': 2,
    'reloadData': False,                # Will re-read your input file and train a new model with the updated data
    'retrainModel': False,              # Will use the currently saved data and train a new model (useful to try different settings without processing the same corpus)
    'minimumProbability': 0.00000001,
    'nbFigures': 5,
    'topicGroups': [[0,1,2,3,4]],
}


misc_sets = {
    'datasetName': 'descrp',
    'dataSource': 'descrp.json',
    'corpusFieldName': 'description',
    'dateFieldName': 'published_date',
    'model_type': 'LDA',
    'json_orientation': 'records',
    'encoding': 'iso8859_14',
    # Advanced settings
    'numberTopics': 20,
    'numberWords': 10,
    'moving_average_size': 2,
    'reloadData': False,                # Will re-read your input file and train a new model with the updated data
    'retrainModel': False,              # Will use the currently saved data and train a new model (useful to try different settings without processing the same corpus)
    'minimumProbability': 0.00000001,
    'nbFigures': 0,
}

covid_settings = {
    # 'datasetName': 'COVID_titles',
    'datasetName': 'COVID_themes',
    'dataSource': 'covid.csv',
    # 'corpusFieldName': 'title',
    'corpusFieldName': 'THEME',
    'dateFieldName': 'debunking_date',
    'roundToDay': True,
    'model_type': 'LDA',
    # Advanced settings
    'numberTopics': 20,
    'numberWords': 10,
    'moving_average_size': 2,
    'reloadData': False,                # Will re-read your input file and train a new model with the updated data
    'retrainModel': False,              # Will use the currently saved data and train a new model (useful to try different settings without processing the same corpus)
    'minimumProbability': 0.00000001,
    'nbFigures': 20,
    # 'topicGroups': [[10,12,17,18]],
    'topicGroups': [[2, 13, 15]],
    'minimumProbability': 0.00000001,
    'distributionInWorksheet': False,
    'addLegend': True,
}

muri_settings = {
    'datasetName': 'MURI',
    'dataSource': 'MURI blog data.json',
    'corpusFieldName': 'post',
    'dateFieldName': 'date',
    'reloadData': False,                # Will re-read your input file and train a new model with the updated data
    'retrainModel': False,              # Will use the currently saved data and train a new model (useful to try different settings without processing the same corpus)
    'start_date': "2015-01-01",         # Optional - will only select items from this date when creating the topic distribution matrix
    'end_date': "2016-01-01",           # Optional - will only select items up to this date when creating the topic distribution matrix
    'numberTopics': 50,
    'numberWords': 10,
    'moving_average_size': 5,
    'minimumProbability': 0.00000001,
    'nbFigures': 5,
    'lang': ('language', 'English'),   # Optional - if specified, will filter by column 'language' whose value is 'English'
}
