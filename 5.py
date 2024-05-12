def merge(*catalogs):
    combined_catalog = ()
    for catalog in catalogs:
        combined_catalog += catalog
    return combined_catalog


catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))


combined_catalog = merge(catalog1, catalog2)


print("Combined Catalog:")
for product in combined_catalog:
    print(product)