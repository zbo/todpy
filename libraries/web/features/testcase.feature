Feature: tod sample test case 01
  open browser, client some place, assert text, close browser

  Scenario: open ms bing site
    Given I open web browser
    When I open page 'http://cn.bing.com/'
    Then I see 'Bing' in the title
    When I input 'microsoft' into textbox with id 'sb_form_q'
    Then I see 'microsoft' in textbox with id 'sb_form_q'
    When I click element with id 'sb_form_go'
    Then I close web browser


