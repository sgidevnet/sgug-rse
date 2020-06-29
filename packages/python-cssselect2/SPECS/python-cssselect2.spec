%global srcname cssselect2
%global py3_prefix python%{python3_pkgversion}

Name:           python-%{srcname}
Version:        0.3.0
Release:        2%{?dist}
Summary:        CSS selectors for Python ElementTree
License:        BSD
URL:            https://%{srcname}.readthedocs.io/
BuildArch:      noarch
Source0:        %pypi_source
# Fedora does not ship pytest's flake8/isort modules

BuildRequires:  %{py3_prefix}-devel
BuildRequires:  %{py3_prefix}-setuptools >= 39.2.0
BuildRequires:  %{py3_prefix}-pytest
BuildRequires:  %{py3_prefix}-pytest-cov
BuildRequires:  %{py3_prefix}-pytest-isort
BuildRequires:  %{py3_prefix}-pytest-runner
BuildRequires:  %{py3_prefix}-tinycss2
BuildRequires:  %{py3_prefix}-webencodings

%description
cssselect2 is a straightforward implementation of CSS3 Selectors for markup
documents (HTML, XML, etc.) that can be read by ElementTree-like parsers,
including cElementTree, lxml, html5lib_, etc.


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide %{py3_prefix}-cssselect2}

%description -n python3-%{srcname}
cssselect2 is a straightforward implementation of CSS3 Selectors for markup
documents (HTML, XML, etc.) that can be read by ElementTree-like parsers,
including cElementTree, lxml, html5lib_, etc.


%prep
%autosetup -n %{srcname}-%{version}
# Skip the flake8 plugin:
sed -i 's/--flake8//' setup.cfg

%build
%py3_build


%install
%py3_install


%check
%{__python3} -m pytest -v
# remove files which are only required for unit tests
rm -rf %{buildroot}%{python3_sitelib}/%{srcname}/tests


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-2
- Rebuilt for Python 3.9

* Tue Mar 17 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 0.3.0-1
- update to 0.3.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 25 2019 Felix Schwarz <fschwarz@fedoraproject.org> 0.2.2-2
- use sources from pypi, packaging fixes

* Thu Oct 24 2019 Felix Schwarz <fschwarz@fedoraproject.org> 0.2.2-1
- update to new upstream version 0.2.2

* Thu May 02 2019 Eric Smith <brouhaha@fedoraproject.org> 0.2.1-3
- Moved Requires to subpackage. Added python_provide.

* Wed May 01 2019 Eric Smith <brouhaha@fedoraproject.org> 0.2.1-2
- Added missing BuildRequires and Requires.

* Tue Apr 30 2019 Eric Smith <brouhaha@fedoraproject.org> 0.2.1-1
- Initial version.

