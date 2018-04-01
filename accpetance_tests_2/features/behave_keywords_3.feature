Feature: Demo3 for various key words used in Behave

  Scenario: Update user details
    Given I login to update details
    When I update following user details "<item_name>" and "<item_detail>"
        |item_name|item_detail           |
        |address  |12 Windsor Castle Raod|
        |contact  |7568199583            |
        |name     |Yoganand              |
        |surname  |Kunche                |
    Then User detail update should be successful
