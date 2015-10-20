Feature: mi note device info page
  mi note is one kind of xiao mi device, make sure info page alive

   Scenario: should open the mi note page
    Given open page 'http://www.mi.com/en/'
    When I click element with class 'nav-item'
     When I click element with text 'Mi Note'
     Then I see the 'Note' in the title