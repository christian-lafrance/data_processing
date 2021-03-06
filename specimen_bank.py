# gets panel members as value using panel name as a key in a dictionary
def get_specimens(panel):
    specimen_bank = {
        '9172': ['9172-01', '9172-02', '9172-03', '9172-04', '9172-05', 
                 '9172-06', '9172-07', '9172-08', '9172-09','9172-10', 
                 '9172-11', '9172-12'],
        'flex': ['9172-01', '9172-02', '9172-03', '9172-04', '9172-05', 
                 '9172-06', '9172-07', '9168-05', '9168-06','9172-11', 
                 '9172-12'],
        '9170': ['9170-01', '9170-02', '9170-03', '9170-04', '9170-05', 
                 '9170-06', '9170-07', '9170-08', '9170-09',
                 '9170-10', '9170-11', '9170-12', '9170-13'],
        'RR': ['day 1-1', 'day 1-2', 'day 1-3', 'day 1-4', 'day 1-5', 
               'day 1-6', 'day 1-7', 'day 2-1', 'day 2-2',
               'day 2-3', 'day 2-4', 'day 2-5', 'day 2-6', 'day 2-7', 
               'day 3-1', 'day 3-2', 'day 3-3', 'day 3-4', 
               'day 3-5', 'day 3-6', 'day 3-7', 'day 4-1', 'day 4-2', 
               'day 4-3', 'day 4-4', 'day 4-5', 'day 4-6', 
               'day 4-7', 'day 5-1', 'day 5-2', 'day 5-3', 'day 5-4', 
               'day 5-5', 'day 5-6', 'day 5-7'], 
        '9169':['9169-01', '9169-02', '9169-03', '9169-04', '9169-05', 
                '9169-06', '9169-07', '9169-08', '9169-09', 
                '9169-10', '9169-11', '9169-12', '9169-13', '9169-14', 
                '9169-15', '9169-16', '9169-17', '9169-18', 
                '9169-19', '9169-20', '9169-21', '9169-22', '9169-23', 
                '9169-24', '9169-25', '9169-26', '9169-27', 
                '9169-28', '9169-29', '9169-30', '9169-31', '9169-32', 
                '9169-33', '9169-34', '9169-35', '9169-36', 
                '9169-37', '9169-38', '9169-39', '9169-40', '9169-41', 
                '9169-42', '9169-43', '9169-44', '9169-45', 
                '9169-46', '9169-47', '9169-48', '9169-49', '9169-50', 
                '9169-51', '9169-52', '9169-53', '9169-54', 
                '9169-55', '9169-56', '9169-57', '9169-58', '9169-59', 
                '9169-60', '9169-61', '9169-62', '9169-63', 
                '9169-64', '9169-65', '9169-66', '9169-67', '9169-68', 
                '9169-69', '9169-70', '9169-71', '9169-72', 
                '9169-73'], 
        'Gilead 1':[str(i) for i in range(84)], 
        'Gilead 2': ['g'+str(i) for i in range(1,111)],
        'Prozone':['dxp005', 'dxp006', 'dxp017', 'dxp026', 'dxp027', 'dxp032', 
                   'dxp040', 'dxp047', 'dxp048', 'dxp049', 'dxp050', 'dxp063', 
                   'dxp069', 'dxp073', 'dxp081', 'dxp084', 'dxp086', 'dxp087', 
                   'dxp094', 'dxp099', 'boca007','boca028', 'boca029', 
                   'boca031', 'boca080', 'boca084','boca099', 'boca121', 
                   'boca135', 'boca139', 'boca142','boca143', 'boca150', 
                   'boca155', 'boca157', 'boca161', 
                   'boca163', 'boca169', 'boca175', 'boca188'],
        '9172/9168 Hybrid': ['9172-01', '9172-02', '9172-04', '9172-07',
                             '9168-05', '9168-06', '9172-12']
    }

    return specimen_bank[panel]
