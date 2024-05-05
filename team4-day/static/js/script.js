// script.js

// チェックボックスの色をトグルする関数
function toggleColor(element) {
    element.classList.toggle('active');
}

// 「じゅんびできたよ！！」ボタンがクリックされたときに実行される関数
function redirectReady() {
    // すべてのアイテムが選択されているかどうかを確認
    var allItemsChecked = checkAllItemsSelected();
    
    // すべてのアイテムが選択されている場合
    if (allItemsChecked) {
        // 準備完了ページにリダイレクト
        window.location.href = '/ready';
    } else {
        // 未完了ページにリダイレクト
        window.location.href = '/incomplete';
    }
}

// すべてのアイテムが選択されているかどうかを確認する関数
function checkAllItemsSelected() {
    var dailyItems = document.getElementsByName('daily_items');
    var variableItems = document.getElementsByName('variable_items');
    
    // すべての「まいにちじゅんび」アイテムが選択されているかをチェック
    var allDailyItemsChecked = true;
    for (var i = 0; i < dailyItems.length; i++) {
        if (!dailyItems[i].checked) {
            allDailyItemsChecked = false;
            break;
        }
    }
    
    // すべての「このひだけじゅんび」アイテムが選択されているかをチェック
    var allVariableItemsChecked = true;
    for (var j = 0; j < variableItems.length; j++) {
        if (!variableItems[j].checked) {
            allVariableItemsChecked = false;
            break;
        }
    }
    
    // すべてのアイテムが選択されているかどうかを返す
    return allDailyItemsChecked && allVariableItemsChecked;
}


