# Created by pyp2rpm-3.3.2
%global pypi_name pycotap

Name:           python-%{pypi_name}
Version:        1.1.0
Release:        6%{?dist}
Summary:        A tiny test runner that outputs TAP results to standard output

License:        MIT
URL:            https://el-tramo.be/pycotap
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
pycotap is a simple Python test runner for unit tests that outputs Test Anything
Protocol results directly to standard output.Contrary to other TAP runners
for Python, pycotap prints TAP (and *only* TAP) to standard output
instead of to a separate file, allowing you to pipe it directly to TAP pretty
printers and processors.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
pycotap is a simple Python test runner for unit tests that outputs Test Anything
Protocol results directly to standard output.Contrary to other TAP runners
for Python, pycotap prints TAP (and *only* TAP) to standard output
instead of to a separate file, allowing you to pipe it directly to TAP pretty
printers and processors.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install
find %{buildroot}/%{python3_sitelib} -name '*.py' | xargs sed -i '/^#!/d'

%files -n python3-%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 18 2019 Shlomi Fish <shlomif@shlomifish.org> - 1.1.0-1
- Initial package.
