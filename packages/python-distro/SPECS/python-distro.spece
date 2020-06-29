%global pypi_name distro
%if 0%{?rhel} && 0%{?rhel} <= 7
%bcond_with python3
%bcond_without python2
%else
%bcond_without python3
%bcond_with python2
%endif

Name:           python-%{pypi_name}
Version:        1.5.0
Release:        3%{?dist}
Summary:        Linux Distribution - a Linux OS platform information API

License:        ASL 2.0
URL:            https://github.com/nir0s/distro
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
%global _description \
The distro (for: Linux Distribution) package provides information about the\
Linux distribution it runs on, such as a reliable machine-readable ID, or\
version information.\
\
It is a renewed alternative implementation for Python's original\
platform.linux_distribution function, but it also provides much more\
functionality. An alternative implementation became necessary because\
Python 3.5 deprecated this function, and Python 3.7 is expected to remove it\
altogether. Its predecessor function platform.dist was already deprecated since\
Python 2.6 and is also expected to be removed in Python 3.7. Still, there are\
many cases in which access to that information is needed. See Python issue 1322\
for more information.

%description %{_description}

%if %{with python2}
%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
BuildRequires:  python2-devel
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:  python-setuptools
BuildRequires:  pytest
%else
BuildRequires:  python2-setuptools
BuildRequires:  python2-pytest
%endif
%if 0%{?fedora}
Suggests:       /usr/bin/lsb_release
%endif

%description -n python2-%{pypi_name} %{_description}

Python 2 version.
%endif

%if %{with python3}
%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
%if 0%{?fedora}
Suggests:       /usr/bin/lsb_release
%endif

%description -n python3-%{pypi_name} %{_description}

Python 3 version.
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif

%install
%if %{with python2}
%py2_install
%endif
%if %{with python3}
%py3_install
%endif

%if %{with python2}
%files -n python2-%{pypi_name}
%doc CHANGELOG.md CONTRIBUTORS.md README.md
%license LICENSE
%{python2_sitelib}/%{pypi_name}-*.egg-info/
%{python2_sitelib}/%{pypi_name}.py*
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%doc CHANGELOG.md CONTRIBUTORS.md README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}-*.egg-info/
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/__pycache__/%{pypi_name}.*
%endif

%{_bindir}/distro

%check
%if %{with python2}
%{__python2} -m pytest tests -v
%endif
%if %{with python3}
%{__python3} -m pytest tests -v
%endif

%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-3
- Rebuilt for Python 3.9

* Mon May 11 2020 Stephen Gallagher <sgallagh@redhat.com> - 1.5.0-2
- Fix Python configuration for ELN/RHEL 9
- Rework bconds for Python now that there are no Fedoras left that should
  use Python2

* Tue Mar 31 2020 Marek Blaha <mblaha@redhat.com> - 1.5.0-1
- rebase to distro 1.5.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 04 2019 Marek Blaha <mblaha@redhat.com> - 1.4.0-1
- rebase to distro 1.4.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 30 2018 Marek Blaha <mblaha@redhat.com> - 1.3.0-5
- do not build python2 version for Fedora 30+

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-3
- Rebuilt for Python 3.7

* Tue May 29 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-2
- run tests by pytest, not by tox, there is no tox.ini

* Thu May 10 2018 Miroslav Suchý <msuchy@redhat.com> 1.3.0-1
- rebase to distro 1.3.0

* Tue Jan 02 2018 Miroslav Suchý <msuchy@redhat.com> 1.2.0-1
- run tests
- rebase to distro 1.2.0

* Mon Mar 20 2017 Miroslav Suchý <msuchy@redhat.com> 1.0.3-1
- rebase to 1.0.3

* Tue Jan 24 2017 Miroslav Suchý <msuchy@redhat.com> 1.0.2-3
- typo in license macro

* Tue Jan 24 2017 Miroslav Suchý <msuchy@redhat.com> 1.0.2-2
- add license macro for el6

* Tue Jan 24 2017 Miroslav Suchý <msuchy@redhat.com> 1.0.2-1
- update to 1.0.2
- 1415667 - require python-argparse on EL6

* Tue Jan 03 2017 Miroslav Suchý <msuchy@redhat.com> 1.0.1-2
- soft deps on lsb_release

* Sun Jan 01 2017 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.1-1
- Update to 1.0.1
- Provide only one copy of $bindir/distro
- Cleanups in spec

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-7
- Rebuild for Python 3.6

* Thu Oct 06 2016 Miroslav Suchý <msuchy@redhat.com> 1.0.0-6
- polish spec according the package review

* Wed Oct 05 2016 Miroslav Suchý 1.0.0-5
- use python3 in /usr/bin/distro on Fedoras

* Wed Oct 05 2016 Miroslav Suchý 1.0.0-4
- use python3 in /usr/bin/distro on Fedoras

* Wed Oct 05 2016 Miroslav Suchý 1.0.0-3
- python2 subpackages only on rhel
- correct description

* Wed Oct 05 2016 Miroslav Suchý 1.0.0-2
- require lsb_release

* Wed Oct 05 2016 Miroslav Suchý 1.0.0-1
- initial packaging

