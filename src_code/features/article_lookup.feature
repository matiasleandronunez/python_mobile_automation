Feature: Article lookup

  Scenario Outline: Look up an article
    Given I look up <keyword>
    When I click on the first result displayed
    Then wikipedia article titled <article_title> is displayed

    Examples:
    |keyword|article_title|
    |hungary|Hungary      |