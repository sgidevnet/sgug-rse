%bcond_without tests

%global commit 8ea7a1a5599ad15411f1a9f54321df5a357d41e1
%global shortcommit %(c=%{commit}; echo ${c:0:7})


%global pypi_name airspeed

%global _description %{expand:
Airspeed is a powerful and easy-to-use templating engine for Python that aims
for a high level of compatibility with the popular Velocity library for Java.

- Compatible with Velocity templates
- Compatible with Python 2.6 and greater, including Jython
- Features include macros definitions, conditionals, sub-templates and much more
- Airspeed is already being put to serious use
- Comprehensive set of unit tests; the entire library was written test-first
- Reasonably fast
- A single Python module of a few kilobytes, and not the 500kb of Velocity
- Liberal licence (BSD-style)}

Name:           python-%{pypi_name}
Version:        0.5.16
Release:        2%{?dist}
Summary:        A lightweight template engine compatible with Velocity

License:        BSD
URL:            %pypi_url
Source0:        https://github.com/purcell/%{pypi_name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildArch:      noarch

%{?python_enable_dependency_generator}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist cachetools}
BuildRequires:  %{py3_dist six}
BuildRequires:  %{py3_dist setuptools}
%if %{with tests}
BuildRequires:  %{py3_dist nose}
BuildRequires:  %{py3_dist coverage}
%endif
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{commit}
rm -rf %{pypi_name}.egg-info

find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

%install
%py3_install

%check
%if %{with tests}
%{__python3} setup.py test
%endif

%files -n python3-%{pypi_name}
%license LICENCE
%doc README.md
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}

%changelog
* Thu Jun 25 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.16-2
- Explicitly BR setuptools

* Sun Jun 21 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.16-1
- Update to 0.5.16

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.15-2
- Rebuilt for Python 3.9

* Fri May 01 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.15-1
- Update to latest release
- Use git release for tests

* Tue Apr 21 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.14-1
- Update 0.5.14
- use github commit hash, upstream did not tag release

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 23 2019 Aniket Pradhan <major AT fedoraproject DOT org> - 0.5.13-1
- Upgraded to v0.5.12

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.12-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 29 2019 Aniket Pradhan <major AT fedoraproject DOT org> - 0.5.12-1
- Upgraded to v0.5.12

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.11-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.11-1
- Initial build
