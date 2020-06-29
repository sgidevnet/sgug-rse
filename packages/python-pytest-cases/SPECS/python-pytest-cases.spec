Name:		python-pytest-cases
Version:	1.11.1
Release:	3%{?dist}
Summary:	Separate test code from test cases in pytest

License:	BSD
URL:		https://pypi.org/project/pytest-cases/
Source0:	%{pypi_source pytest-cases}

BuildArch:	noarch
BuildRequires:	pyproject-rpm-macros

%description
%{summary}.

%package -n python3-pytest-cases
Summary: %{summary}

%description -n python3-pytest-cases
%{summary}.

%prep
%autosetup -n pytest-cases-%{version}
cat >pyproject.toml <<EOF
[build-system]
requires = [
    "decopatch",
    "pytest-runner",
    "pytest-steps",
    "setuptools_scm",
    "pypandoc",
    "six"]
build-backend = "setuptools.build_meta"
EOF

sed -r -i "s/'pandoc', //" setup.py

mv -i -v pytest_cases/tests/conftest.py .

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
# Tests rely on a fixture defined by pytest-harvest. I don't want to package this
# just to run some summary in tests. Let's just skip this.
find pytest_cases/tests/ -name '*.py' -exec \
  sed -r -i 's/def test_synthesis\(module_results_dct\)/def _disabled_test_synthesis\(module_results_dct\)/' {} \;

%{__python3} -m pytest -v \
  --ignore pytest_cases/tests/meta/test_all.py # those tests fail with pytest-4

%files -n python3-pytest-cases
%license LICENSE
%doc README.md
%{python3_sitelib}/pytest_cases/
%{python3_sitelib}/pytest_cases-%{version}.dist-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.11.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.11.1-1
- Initial packaging
