#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-jersey-json
Version  : 1.17.1
Release  : 3
URL      : https://repo1.maven.org/maven2/com/sun/jersey/jersey-json/1.17.1/jersey-json-1.17.1.jar
Source0  : https://repo1.maven.org/maven2/com/sun/jersey/jersey-json/1.17.1/jersey-json-1.17.1.jar
Source1  : https://repo1.maven.org/maven2/com/sun/jersey/jersey-json/1.17.1/jersey-json-1.17.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : CDDL-1.1 GPL-2.0-only
Requires: mvn-jersey-json-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-jersey-json package.
Group: Data

%description data
data components for the mvn-jersey-json package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-json/1.17.1
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-json/1.17.1/jersey-json-1.17.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-json/1.17.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-json/1.17.1/jersey-json-1.17.1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/sun/jersey/jersey-json/1.17.1/jersey-json-1.17.1.jar
/usr/share/java/.m2/repository/com/sun/jersey/jersey-json/1.17.1/jersey-json-1.17.1.pom
