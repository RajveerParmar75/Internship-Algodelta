class User {
  String name, address, document;
  int phoneNo;
  num interest;
  User(this.name, this.address, this.phoneNo, this.interest, this.document);
  static Map<String, dynamic> ConvertToUser(String name, String address,
          String document, int mobileNumber, num interest) =>
      {
        'name': name,
        'address': address,
        'document': document,
        'mobileNumber': mobileNumber,
        'interest': interest
      };
}
