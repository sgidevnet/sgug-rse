%global srcname jep

%global desc \
Java Embedded Python\
JEP embeds CPython in Java through JNI and is safe to use in a\
heavily threaded environment.\
\
Some benefits of embedding CPython in a JVM:\
    Using the native Python interpreter may be much faster than\
    alternatives.\
    Python is mature, well supported, and well documented.\
    Access to high quality Python modules, both native CPython\
    extensions and Python-based.\
    Compilers and assorted Python tools are as mature as the\
    language.\
    Python is an interpreted language, enabling scripting of\
    established Java code without requiring recompilation.\
    Both Java and Python are cross platform, enabling deployment\
    to different operating system.

Name:           python-%{srcname}
Version:        3.9.0
Release:        5%{?dist}
Summary:        Embed Python in Java

License:        zlib
URL:            https://github.com/ninia/%{srcname}
Source0:        %{url}/archive/v%{version}.tar.gz
# rhbz#1792062 Stop using daemon thread in test using sub-interpreter for python 3.9
Patch0:         %{url}/commit/a31d461c6cacc96de68d68320eaa83e19a45d0cc.patch

BuildRequires:  python3-devel
BuildRequires:  python3-numpy

BuildRequires:  java-devel
BuildRequires:  gcc

Requires:       java-headless

%description %desc

%package     -n python3-%{srcname}
Summary:        Embed Python in Java
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %desc

%package javadoc
Summary:        Javadoc files for %{name}
BuildArch:      noarch

%description javadoc
%{summary}.


%prep
%autosetup -p1 -n%{srcname}-%{version}
find . -name \*.jar -print -delete


%build
export JAVA_HOME=%{_prefix}/lib/jvm/java
CFLAGS="$RPM_OPT_FLAGS" %py3_build
%{__python3} setup.py javadoc


%install
export JAVA_HOME=%{_prefix}/lib/jvm/java
%py3_install

# install javadoc
install -dm755 %{buildroot}%{_javadocdir}/%{name}
cp -pr javadoc/* %{buildroot}%{_javadocdir}/%{name}


%check
export JAVA_HOME=%{_prefix}/lib/jvm/java
# be more verbose about tests, FIXME ugly hack!
sed -i -r 's:TextTestRunner\(:\0verbosity=2:' src/test/python/runtests.py
%{__python3} setup.py test || cat *.log
# jdk may crash aka 'An error report file with more information is saved'
: ### core dumps ###
cat core* || :


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%doc AUTHORS release_notes/
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/%{srcname}-%{version}-py*.egg-info
%{_bindir}/%{srcname}

%files javadoc
%license LICENSE
%{_javadocdir}/%{name}/


%changelog
* Sat Jun 06 2020 Raphael Groner <raphgro@fedoraproject.org> - 3.9.0-5
- add patch for python 3.9, avoid daemon thread, rhbz#1792062

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.9.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.9.0-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 31 2019 Raphael Groner <projects.rg@smart.ms> - 3.9.0-1
- new version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.8.2-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 10 2019 Raphael Groner <projects.rg@smart.ms> - 3.8.2-3
- adjust execution of tests to fix for python 3.8, rhbz#1706238
- fix path of module installation

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 17 2018 Raphael Groner <projects.rg@smart.ms> - 3.8.2-1
- new version

* Thu Jul 12 2018 Raphael Groner <projects.rg@smart.ms> - 3.8.0-1
- new version

* Sat Jul 07 2018 Raphael Groner <projects.rg@smart.ms> - 3.8-0.1.rc
- new version (RC) with support for Python 3.7
- generate javadoc because not provided in tarball any more
- drop optional python2

* Sat Jul 07 2018 Raphael Groner <projects.rg@smart.ms> - 3.7.1-1
- new version

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.7.0-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 02 2017 Raphael Groner <projects.rg@smart.ms> - 3.7.0-2
- drop precompiled jar files
- be more verbose about tests
- add javadoc subpackage
- move interpreter script into python3 subpackage
- add release_notes folder to documentation
- handle readme file properly

* Tue Aug 15 2017 Raphael Groner <projects.rg@smart.ms> - 3.7.0-1
- initial
