# TODO:
# - build
#
# Conditional build:
%bcond_without	javadoc		# don't build javadoc
%bcond_without	tests		# don't build and run tests
%bcond_with	java_sun	# build with gcj

%if "%{pld_release}" == "ti"
%define	with_java_sun	1
%endif

%include	/usr/lib/rpm/macros.java

%define		srcname		modello
Summary:	Data Model toolkit
Name:		java-modello
Version:	1.0.1
Release:	0.1
License:	BSD-like
Group:		Libraries/Java
# svn export http://svn.codehaus.org/modello/tags/modello-1.0.1/
Source0:	%{srcname}-%{version}.tar.bz2
# Source0-md5:	ca3eefd13ff5f2e087d44a9c0560ed87
URL:		http://modello.codehaus.org/
%{!?with_java_sun:BuildRequires:	java-gcj-compat-devel}
%{?with_java_sun:BuildRequires:	java-sun}
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Modello is a Data Model toolkit in use by the Maven 2 Project.

%package javadoc
Summary:	Online manual for %{srcname}
Summary(pl.UTF-8):	Dokumentacja online do %{srcname}
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Documentation for %{srcname}.

%description javadoc -l pl.UTF-8
Dokumentacja do %{srcname}.

%description javadoc -l fr.UTF-8
Javadoc pour %{srcname}.

%package examples
Summary:	Examples for %{name}
Summary(pl.UTF-8):	Przykłady dla pakietu %{name}
Group:		Documentation
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description examples
Demonstrations and samples for %{srcname}.

%description examples -l pl.UTF-8
Pliki demonstracyjne i przykłady dla pakietu %{srcname}.

%prep
%setup -q -n %{srcname}-%{version}

%build
#CLASSPATH=$(build-classpath jaxen)
#export CLASSPATH
export JAVA_HOME="%{java_home}"

install -d build
#%%javac -classpath $CLASSPATH -source 1.5 -target 1.5 -d build $(find -name '*.java')
%javac -source 1.5 -target 1.5 -d build $(find -name '*.java')

%if %{with javadoc}
%javadoc -d apidocs \
	%{?with_java_sun:org.jaxen} \
	$(find src/java/main/org/jaxen/ -name '*.java')
%endif

%jar -cf %{srcname}-%{version}.jar -C build .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
cp -a %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

# javadoc
%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -a apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%{_javadir}/%{srcname}-%{version}.jar
%{_javadir}/%{srcname}.jar
%doc LICENSE.txt

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}
%endif
