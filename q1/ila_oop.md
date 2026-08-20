# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation

Encapsulation can be applied in this scenario by initiating a class for the `Product` that contains the `name`, `price`, and quantity fields with methods such as `restock` and `sell` acting as a single unit. Private fields prevent any external funtion from directly modifying values/stock or enabling negative prices, ensuring that the only changes will only occur through controlled methods. Performing this improves design by ruling out invalid inventory states and enforcing data integrity in one clean, maintainable state.

CLASS Product
    PRIVATE name: STRING 
    PRIVATE price: FLOAT
    PRIVATE quantity: INTEGER

    CREATE(name, price, quantity)
        THIS.name = name
        THIS.price = price
        THIS.quantity = quantity
    END CREATE
    
    PUBLIC FUNCTION sell(amount : INTEGER) -> BOOLEAN
        IF amount > 0 AND amount <= THIS.quantity THEN
            THIS.quantity = THIS.quantity - amount
            RETURN TRUE
        END IF
        RETURN FALSE
    END FUNCTION
END CLASS

### 2. Abstraction

Abstraction enables us to expose simple high-level commands like `inventory_report` or `checkout` while hiding complex internal processes like updating database values, assessing financial records, or applying discounts. The rest of the program interacts with simple method interfaces without needing to know how internal calculations are processed. This drastically simplifies the system, reduces code coupling, and allows the underlying implementation to change without interfering other parts of the application.

CLASS Inventory
    PUBLIC PROCEDURE processSale(product: Product, quantity: INTEGER)
        // Hides complex execution steps from the caller
        IF product.sell(quantity) THEN
            CALL THIS.updateLedger(product, quantity)
            CALL THIS.printReceipt(product, quantity)
        END IF
    END PROCEDURE
END CLASS

### 3. Inheritance

Inheritance lets specialized items to inherit common attributes such as `name`,`price` and `quantity` from a base `Product` class (For example, `Beverages` for softdrinks with returnable glass bottles). The subclasses can then freely add specific attributes like `expiration_date` without duplicating existing general code, minimizing redundant code, highlights reusability, and makes adding new store categories effortless.

CLASS Perishables EXTENDS Product
    PRIVATE expirationDate: STRING

    CREATE(name, price, quantity, expirationDate)
        BASE(name, price, quantity)
        THIS.expirationDate = expirationDate
    END CREATE
END CLASS

CLASS Beverages EXTENDS Product
    PRIVATE depositFee: FLOAT

    CREATE(name, price, quantity, depositFee)
        BASE(name, price, quantity)
        THIS.depositFee = depositFee
    END CREATE
END CLASS

### 4. Polymorphism

Polymorphism allows different product types to implement their own particular version of a colllective method, like `calculateTotalCost(quantity)`. To illustrate, standart items compute for the total cost of items via simple multiplication, whereas `Beverages` could add a bottle deposit fee or `Perishables` might apply discounts for goods nearing expiration. The main inventory can iterate through lists of diverse `Product` objects and execute calculations without having the need to check for conditions for every single item type, concluding in a much more efficient and cleaner code.

CLASS Perishables EXTENDS Product
    OVERRIDE FUNCTION calculateTotalCost(quantity: INTEGER) -> FLOAT
        SET basePrice = THIS.getPrice() * quantity
        IF THIS.isNearExpiry() THEN
            RETURN basePrice * 0.8 // 20% discount
        END IF
        RETURN basePrice
    END FUNCTION
END CLASS

CLASS Beverages EXTENDS Product
    OVERRIDE FUNCTION calculateTotalCost(quantity: INTEGER) -> FLOAT
        RETURN (This.getPrice() + This.depositFee) * quantity
    END FUNCTION
END CLASS

## Reflection

Among the four pillars, Encapsulation would be the most impactful pillar for improving the sari-sari store inventory system. In a procedural approach, inventory management often fails because independent variables (like separate arrays or lists for names, prices, and stock) can easily fall out of sync, or stock values can be directly set to invalid numbers from anywhere in the script. Encapsulation solves this fundamental issue by grouping related attributes together into self-contained objects and restricting direct variable access. By protecting core data like stock quantities behind validated class methods, the inventory system guarantees state reliability and eliminates the risk of errors across the application.