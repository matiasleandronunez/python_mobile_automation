Feature: Article lookup

  Scenario Outline: Look up an article
    Given I look up <keyword>
    When I click on the first result displayed
    Then wikipedia article titled <article_title> with subtext <sub_text> is displayed

    Examples:
    |keyword|article_title|sub_text                 |
    |hungary|Hungary      |Country in Central Europe|