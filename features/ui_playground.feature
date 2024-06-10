Feature: UI Playground Test Automation

  Scenario: Verify home page titles and links
    Given I navigate to the UI Playground home page
    Then the page title should be "UI Test Automation Playground"
    And the h3 link texts should be
      | link_text           |
      | Dynamic ID          |
      | Class Attribute     |
      | Hidden Layers       |
      | Load Delay          |
      | AJAX Data           |
      | Client Side Delay   |
      | Click               |
      | Text Input          |
      | Scrollbars          |
      | Dynamic Table       |
      | Verify Text         |
      | Progress Bar        |
      | Visibility          |
      | Sample App          |
      | Mouse Over          |
      | Non-Breaking Space  |
      | Overlapped Element  |
      | Shadow DOM          |

  Scenario: Click dynamic link and button
    Given I navigate to the UI Playground home page
    When I click the "Dynamic ID" link
    Then the button with dynamic ID should be visible and clickable
