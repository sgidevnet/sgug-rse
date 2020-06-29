# Enabled by default
# If the package needs to download data for the test which cannot be done in
# koji, these can be disabled in koji by using `bcond_with` instead, but the
# tests must be validated in mock with network enabled like so:
# mock -r fedora-rawhide-x86_64 rebuild <srpm> --enable-network --rpmbuild-opts="--with tests"
%bcond_without tests

%global pypi_name sciunit

# For scidash
%global scidash_commit 1df0411e74ce35e5b6e748f81cf0159acedab201
%global scidash_shortcommit     %(c=%{scidash_commit}; echo ${c:0:7})

# for sciunit
%global commit  f49d2fb5a108c4d86aee42dd840af7a8e17b382f
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global _description %{expand:
A framework for validating scientific models by creating
experimental-data-driven unit tests.}

Name:           python-%{pypi_name}
Version:        0.2.2.2
Release:        3%{?dist}
Summary:        Framework for test-driven validation of scientific models

License:        MIT
URL:            https://pypi.org/pypi/%{pypi_name}

# For tagged releases on Github: pypi does not include docs etc.
# Source0:        https://github.com/scidash/%%{pypi_name}/archive/%%{version}/%%{pypi_name}-%%{version}.tar.gz
Source0:        https://github.com/scidash/%{pypi_name}/archive/%{commit}/%{pypi_name}-%{shortcommit}.tar.gz

# Required for tests
# https://github.com/scidash/sciunit/blob/0.2.2/test.sh#L3
Source1:        https://github.com/scidash/scidash/archive/%{scidash_commit}/scidash-%{scidash_shortcommit}.tar.gz

BuildArch:      noarch

%{?python_enable_dependency_generator}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist beautifulsoup4}
BuildRequires:  %{py3_dist cerberus}
BuildRequires:  %{py3_dist pip}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist setuptools}

%if %{with tests}
BuildRequires:  %{py3_dist cypy}
BuildRequires:  %{py3_dist gitpython}
BuildRequires:  %{py3_dist ipython}
BuildRequires:  %{py3_dist ipykernel}
BuildRequires:  %{py3_dist jupyter-client}
BuildRequires:  %{py3_dist nbformat}
BuildRequires:  %{py3_dist nbconvert}
BuildRequires:  %{py3_dist pandas}
BuildRequires:  %{py3_dist quantities}
%endif

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        Documentation for %{name}

%description doc  %_description

%prep
%autosetup -n %{pypi_name}-%{commit}
rm -rf %{pypi_name}.egg-info

# Update requirements, our package does not provide bs4
# Remove versioned dependency on quantities
# Remove backports.tempfile, we use what's in py3
sed -i -e 's/bs4/beautifulsoup4/' -e 's/quantities.*/quantities/' -e '/backports/ d' requirements.txt
sed -i -e 's/backports.tempfile/tempfile/' sciunit/utils.py

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

PYTHONPATH=./build/lib/ sphinx-build-%{python3_version} docs/source html
rm -rf html/{.doctrees,.buildinfo,.nojekyll} -vf

%install
%py3_install

%check
%if %{with tests}
# https://github.com/scidash/sciunit/blob/master/test.sh
%{__tar} -xf %{SOURCE1}
mv scidash-%{scidash_commit} ../scidash
# Disable test that requires it to be a git repo by adding the necessary decorator
sed -i '/def test_versioned/i  \ \ \ \ @unittest.skip' sciunit/unit_test/utils_tests.py
PYTHONPATH=%{buildroot}/%{python3_sitelib} %{__python3} -m sciunit.unit_test buffer
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}
%{_bindir}/%{pypi_name}

%files doc
%license LICENSE
%doc README.md
%doc html

%changelog
* Thu Jun 25 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.2.2-3
- Explicitly BR setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.2.2-2
- Rebuilt for Python 3.9

* Fri May 22 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.2.2-1
- Update to new release
- Includes fix for py3.9
- https://bugzilla.redhat.com/show_bug.cgi?id=1838486

* Thu May 07 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.2-1
- Update as per review comments #1827957
- Remove extra provides
- Improve description for doc sub package

* Sat Apr 25 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.2-1
- Initial build
