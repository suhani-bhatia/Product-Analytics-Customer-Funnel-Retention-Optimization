import pandas as pd

def load_and_prepare_data(file_path):
    df = pd.read_csv(file_path)

    df = df.dropna()

    df.columns = [
        "customer_id", "gender", "age", "city", "membership",
        "total_spent", "items_purchased", "avg_rating",
        "discount_applied", "days_since_last_purchase", "satisfaction"
    ]

    return df


def compute_funnel(df):
    total_users = df["customer_id"].nunique()

    engaged_users = df[df["items_purchased"] >= df["items_purchased"].median()]["customer_id"].nunique()

    high_value_users = df[df["total_spent"] > df["total_spent"].quantile(0.75)]["customer_id"].nunique()

    engagement_rate = engaged_users / total_users
    high_value_rate = high_value_users / engaged_users

    return {
        "total_users": total_users,
        "engaged_users": engaged_users,
        "high_value_users": high_value_users,
        "engagement_rate": engagement_rate,
        "high_value_rate": high_value_rate
    }


def compute_retention(df):
    retained = df[df["days_since_last_purchase"] <= 30].shape[0]
    churned = df[df["days_since_last_purchase"] > 30].shape[0]
    total = df.shape[0]

    retention_rate = retained / total

    return {
        "retained": retained,
        "churned": churned,
        "retention_rate": retention_rate
    }