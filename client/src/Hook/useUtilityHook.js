export default function useUtilityHook() {
  const firstLetterUppercase = (name) => {
    const splitName = name.split("_");
    const newName = splitName
      .map((item) => item.charAt(0).toUpperCase() + item.slice(1))
      .join(" ");
    return newName;
  };

  const truncateText = (text, len) => {
    if (text.length > len) {
      const newText = text.slice(0, len);
      return newText + "...";
    }
    return text;
  };

  const formatNumber = (amount) => {
    if (amount == null) {
      return "Invalid amount";
    }

    const newAmount = typeof amount === "string" ? parseFloat(amount) : amount;

    if (isNaN(newAmount)) {
      return "Invalid input";
    }

    const formattedAmount = newAmount.toLocaleString("en-US", {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2,
    });

    return formattedAmount;
  };

  return { firstLetterUppercase, truncateText, formatNumber };
}
