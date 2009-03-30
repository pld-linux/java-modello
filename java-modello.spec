# TODO:
# - package maven and plexus and THEN try to build it from sources
# - dependencies (plexus?)
#
%include	/usr/lib/rpm/macros.java
#
%define		srcname		modello
Summary:	Data Model toolkit
Name:		java-modello
Version:	1.0.1
Release:	0.1
License:	BSD-like
Group:		Libraries/Java
Source0:	http://repository.codehaus.org/org/codehaus/modello/modello-core/%{version}/modello-core-%{version}.jar
# Source0-md5:	d808a73a462dfff839662ff04872fc28
Source1:	http://repository.codehaus.org/org/codehaus/modello/modello-maven-plugin/%{version}/modello-maven-plugin-%{version}.jar
# Source1-md5:	25720daca831f5d1a6ced068551a43f6
Source2:	http://repository.codehaus.org/org/codehaus/modello/modello-plugin-converters/%{version}/modello-plugin-converters-%{version}.jar
# Source2-md5:	0ca084e95cc728ff81bb1d41ec738142
Source3:	http://repository.codehaus.org/org/codehaus/modello/modello-plugin-dom4j/%{version}/modello-plugin-dom4j-%{version}.jar
# Source3-md5:	fc2e2e2ac2461837972e892289aca6a8
Source4:	http://repository.codehaus.org/org/codehaus/modello/modello-plugin-java/%{version}/modello-plugin-java-%{version}.jar
# Source4-md5:	014ca05df577de0204f4949ea19239e9
Source5:	http://repository.codehaus.org/org/codehaus/modello/modello-plugin-jdom/%{version}/modello-plugin-jdom-%{version}.jar
# Source5-md5:	7bc7973910e452ca6d764c09c4195640
Source6:	http://repository.codehaus.org/org/codehaus/modello/modello-plugin-stax/%{version}/modello-plugin-stax-%{version}.jar
# Source6-md5:	6eda5939d8f05d97ae2a46d74c4b0730
Source7:	http://repository.codehaus.org/org/codehaus/modello/modello-plugin-xdoc/%{version}/modello-plugin-xdoc-%{version}.jar
# Source7-md5:	ed81553efa2446e01c34603f5f950a2f
Source8:	http://repository.codehaus.org/org/codehaus/modello/modello-plugin-xml/%{version}/modello-plugin-xml-%{version}.jar
# Source8-md5:	f50caa0c555553c51bbdc62c99bab43d
Source9:	http://repository.codehaus.org/org/codehaus/modello/modello-plugin-xpp3/%{version}/modello-plugin-xpp3-%{version}.jar
# Source9-md5:	52cacdcd875a9e6c92b2c81c78368946
Source10:	http://repository.codehaus.org/org/codehaus/modello/modello-plugin-xsd/%{version}/modello-plugin-xsd-%{version}.jar
# Source10-md5:	a724f4f57aa2b4389df91f6927c58055

# Extracted from one of the .java source files in modello svn repository
Source11:	%{name}-LICENSE.txt

# Is there something more interesting than unit tests?
#Source17:	http://repository.codehaus.org/org/codehaus/modello/modello-test/%{version}/modello-test-%{version}.jar

# Why there is no 1.0.1 release of these jars?
#Source12:	http://repository.codehaus.org/org/codehaus/modello/modello-db-keywords/%{version}/modello-db-keywords-%{version}.jar
#Source13:	http://repository.codehaus.org/org/codehaus/modello/modello-plugin-jpox/%{version}/modello-plugin-jpox-%{version}.jar
#Source14:	http://repository.codehaus.org/org/codehaus/modello/modello-plugin-plexus-registry/%{version}/modello-plugin-plexus-registry-%{version}.jar
#Source15:	http://repository.codehaus.org/org/codehaus/modello/modello-plugin-prevayler/%{version}/modello-plugin-prevayler-%{version}.jar
#Source16:	http://repository.codehaus.org/org/codehaus/modello/modello-plugin-store/%{version}/modello-plugin-store-%{version}.jar

URL:		http://modello.codehaus.org/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Modello is a Data Model toolkit in use by the Maven 2 Project.

%prep
%setup -qc
cp %{SOURCE11} LICENSE.txt

%install

rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}/modello
install %{SOURCE0} $RPM_BUILD_ROOT%{_javadir}/modello/modello-core.1.0.1.jar
install %{SOURCE1} $RPM_BUILD_ROOT%{_javadir}/modello/modello-maven-plugin.1.0.1.jar
install %{SOURCE2} $RPM_BUILD_ROOT%{_javadir}/modello/modello-plugin-converters.1.0.1.jar
install %{SOURCE3} $RPM_BUILD_ROOT%{_javadir}/modello/modello-plugin-dom4j.1.0.1.jar
install %{SOURCE4} $RPM_BUILD_ROOT%{_javadir}/modello/modello-plugin-java.1.0.1.jar
install %{SOURCE5} $RPM_BUILD_ROOT%{_javadir}/modello/modello-plugin-jdom.1.0.1.jar
install %{SOURCE6} $RPM_BUILD_ROOT%{_javadir}/modello/modello-plugin-stax.1.0.1.jar
install %{SOURCE7} $RPM_BUILD_ROOT%{_javadir}/modello/modello-plugin-xdoc.1.0.1.jar
install %{SOURCE8} $RPM_BUILD_ROOT%{_javadir}/modello/modello-plugin-xml.1.0.1.jar
install %{SOURCE9} $RPM_BUILD_ROOT%{_javadir}/modello/modello-plugin-xpp3.1.0.1.jar
install %{SOURCE10} $RPM_BUILD_ROOT%{_javadir}/modello/modello-plugin-xsd.1.0.1.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/%{srcname}
%doc LICENSE.txt
