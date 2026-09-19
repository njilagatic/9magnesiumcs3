# Computational Thinking Exercise

## Smart School Canteen Queue

**Name:** Niane Jair I. Lagatic<br>
**Section:** Magnesium<br>
**Last Name:** Lagatic<br>
**Date:** August 11, 2026

---

## Step 1: Identify the Big Problem

### Main Problem
A local school canteen experiences severe crowding and long wait times during lunch breaks because food ordering, price calculation, and inventory updates are performed by hand without automated tracking or pre-ordering systems.

---

## Step 2: Identify the Sub-Problems

1. Students take a significant amount of time to view choices and decide what to order whilst standing at the cashier counter.
2. The cashier manually caculates the order totals and calculates cash change for every transaction.
3. Canteen staff and students lack real-time visibility into which food items are already out of stock.
4. Physical queue bottlenecks occur because all students wait in a single line despite of whether they are buying a full meal or just a simple drink.

---

## Step 3: Apply Computational Thinking Skills

| Sub-Problem | CT Skill | Proposed Solution |
| :--- | :--- | :--- |
| **1. Order selection delay** | **Abstraction** | Filter out unnecessary counter-side browsing by displaying live digital menu boards outside the queue and providing online menus so students decide before lining up. |
| **2. Manual payment processing** | **Algorithm Design** | Implement an automated system that scans items, calculates totals automatically, and computes change or processes student card payments. |
| **3. Lack of stock visibility** | **Decomposition** | Break inventory management down into per-item counters that decrement upon every purchase and automatically mark items as "Out of Stock" on display screens. |
| **4. Unmanaged queue flow** | **Pattern Recognition** | Identify recurring purchasing patterns and create dedicated lines for quick pre-packaged items versus full cooked meals to optimize line speed. |

---

## Step 4: Algorithmic Solution

### Selected Sub-Problem
Automatic Point of Sale and Payment Calculation (Sub-Problem 2)

### Pseudocode
START
    
    SET OrderTotal = 0
    
    WHILE CustomerIsOrdering IS TRUE DO
        DISPLAY MenuItemList
        INPUT SelectedItem, quantity
        
        IF CheckStock(SelectedItem) >= quantity THEN
            SET ItemCost = getItemPrice(SelectedItem) * quantity
            SET OrderTotal = OrderTotal + ItemCost
            CALL UpdateInventory(SelectedItem, quantity)
        ELSE
            PRINT "This item is out of stock."
        END IF
        
        INPUT ContinueOrdering (YES or NO)
        IF ContinueOrdering == NO THEN
            EXIT WHILE
        END IF
    ENDWHILE
    
    PRINT "Total Amount Due: P" + OrderTotal
    INPUT PaymentMethod (CASH or CARD)
    
    IF PaymentMethod == "CARD" THEN
        INPUT StudentCardBalance
        IF StudentCardBalance >= OrderTotal THEN
            SET NewBalance = StudentCardBalance - OrderTotal
            PRINT "Payment Successful! Remaining Balance: P" + NewBalance
        ELSE
            PRINT "Insufficient card balance. Please use cash or reload card."
        END IF
    ELSE IF PaymentMethod == "CASH" THEN
        INPUT CashReceived
        IF CashReceived >= OrderTotal THEN
            SET ChangeAmount = CashReceived - orderTotal
            PRINT "Payment Successful! Change Due: P" + ChangeAmount
        ELSE
            PRINT "Insufficient cash provided."
        END IF
    END IF
    
    PRINT "Order complete. Printing receipt."  
    
END