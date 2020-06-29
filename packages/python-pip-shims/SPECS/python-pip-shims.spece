%global         pypi_name pip-shims
%global         _description %{expand:This is library used by pipenv.
Author recommends that nothing else than pipenv should depend on this.}

Name:           python-%{pypi_name}
Version:        0.3.2
Release:        5%{?dist}
License:        ISC
URL:            https://github.com/sarugaku/pip-shims
Source0:        https://github.com/sarugaku/pip-shims/archive/%{version}/pip-shims-%{version}.tar.gz
BuildArch:      noarch
Summary:        Pip-shims is a set of compatibility access shims to the pip internal API

%description
%{_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-pip
#Requires:       python3-pip
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{_description}

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
# Disable tests for Py 3.9 rebuild
# the plan is to retire this package during the next update of pipenv
# PYTHONPATH=%%{buildroot}%%{python3_sitelib} %%{__python3} -m pytest -k 'not test_resolution and not test_wheelbuilder\
# and not test_abstract_dist and not test_vcs_support and not test_command and not test_configparser and not test_path_and_url and not test_cache_dir and not test_archive_file and not test_safe_file_cache'

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/pip_shims-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/pip_shims/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-5
- Rebuilt for Python 3.9

* Fri Feb 07 2020 Patrik Kopkan <pkopkan@redhat.com> - 0.3.2-4
- Temporarly skip tests: test_abstract_dist, test_vcs_support

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Tue Aug 13 2019 Patrik Kopkan <pkopkan@redhat.com> - 0.3.2
- initial package
