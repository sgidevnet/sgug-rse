%global srcname parse

Name:           python-%{srcname}
Version:        1.11.1
Release:        7%{?dist}
Summary:        Opposite of format()

License:        BSD
URL:            http://pypi.python.org/pypi/parse
Source0:        %{pypi_source}

BuildArch:      noarch

%global _description \
Parse strings using a specification based on the Python format() syntax.\
\
"parse()" is the opposite of "format()"

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -p1
chmod -x README.rst

%build
%py3_build

%install
%py3_install

%check
%{__python3} test_parse.py

%files -n python3-%{srcname}
%doc README.rst
%{python3_sitelib}/%{srcname}-%{version}-*.egg-info
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/__pycache__/%{srcname}.*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.11.1-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.11.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.11.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.11.1-1
- Update to 1.11.1

* Wed Jan 09 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.8.4-2
- Drop python2 subpackage

* Mon Jul 30 2018 Miro Hrončok <mhroncok@redhat.com> - 1.8.4-1
- Update to 1.8.4

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.6.6-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.6.6-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.6-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Apr 19 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.6.6-3
- Remove unneded BuildRequires
- Use %%python_provde
- Correctly split to python2- subpkg
- Fix spurious-executable-perm
- Don't use %%py3dir

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 15 2015 Matěj Cepl <mcepl@redhat.com> - 1.6.6-1
- Upgrade to the latest upstream (#1291602)

* Mon Dec 14 2015 David King <amigadave@amigadave.com> - 1.6.4-4
- Fix test failure with Python 3.5 (#1291218)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 19 2014 Matěj Cepl <mcepl@redhat.com> - 1.6.4-1
- New upstream release.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Aug 27 2013 Matěj Cepl <mcepl@redhat.com> - 1.6.2-4
- There is no official py3k support for RHEL-6.

* Wed Jul 24 2013 Matěj Cepl <mcepl@redhat.com> - 1.6.2-3
- We actually don't need 2to3.

* Wed Jul 24 2013 Matěj Cepl <mcepl@redhat.com> - 1.6.2-2
- make python3 package as well
- BR python-setuptools
- fix changelog

* Tue Jul 23 2013 Matěj Cepl <mcepl@redhat.com> - 1.6.2-1
- initial package for Fedora
