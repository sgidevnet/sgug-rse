%global srcname tabulate

Name:           python-%{srcname}
Version:        0.8.7
Release:        2%{?dist}
Summary:        Pretty-print tabular data in Python, a library and a command-line utility

License:        MIT
URL:            https://pypi.python.org/pypi/tabulate
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
The main use cases of the library are:

* printing small tables without hassle: just one function call, formatting is
  guided by the data itself
* authoring tabular data for lightweight plain-text markup: multiple output
  formats suitable for further editing or transformation
* readable presentation of mixed textual and numeric data: smart column
  alignment, configurable number formatting, alignment by a decimal point}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
# Test deps
BuildRequires:  python3dist(nose)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(wcwidth)
# widechars support
Recommends:     python%{python3_version}dist(wcwidth)

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE
%doc README README.md
%{_bindir}/%{srcname}
%{python3_sitelib}/%{srcname}*.egg-info/
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/__pycache__/%{srcname}.*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.7-2
- Rebuilt for Python 3.9

* Sun Mar 29 2020 Aniket Pradhan <major AT fedoraproject DOT org> - 0.8.7-1
- Update to 0.8.7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Aniket Pradhan <major AT fedoraproject DOT org> - 0.8.6-1
- Update to 0.8.6

* Wed Nov 20 12:21:20 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.5-2
- Remove all useless changes in spec

* Fri Oct 25 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.5-1
- Update to 0.8.5

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.3-3
- Remove py2 subpackage

* Sat Jan 26 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.3-2
- Fix FTBFS

* Sat Jan 26 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.3-1
- Update to latest upstream release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Steve Traylen <steve.traylen@cern.ch> - 0.8.2-1
- Update to 0.8.2, Correct source URL.

* Tue Oct 03 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1
- Run more tests

* Sun Oct 01 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.7.5-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 29 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.7.5-2
- Drop multiple versions of bins

* Tue Nov 24 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.7.5-1
- Initial package
