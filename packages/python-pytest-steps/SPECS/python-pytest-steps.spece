Name:		python-pytest-steps
Version:	1.7.2
Release:	2%{?dist}
Summary:	Create step-wise / incremental tests in pytest

License:	BSD
URL:		https://pypi.org/project/pytest-steps/
Source0:	%{pypi_source pytest-steps}

BuildArch:	noarch
BuildRequires:	pyproject-rpm-macros

%description
%{summary}.

%package -n python3-pytest-steps
Summary: %{summary}
%{?python_provide:%python_provide python3-pytest-steps}

%description -n python3-pytest-steps
%{summary}.

%prep
%autosetup -n pytest-steps-%{version}

# upstream has a pyproject.toml file, but it does not have enough stuff.
cat >pyproject.toml <<EOF
[build-system]
requires = ["pytest-runner",
	    "pytest-harvest",
	    "setuptools_scm",
	    "pypandoc",
	    "six",
	    "wheel",
	    "wrapt",
	    "pandas",
	    "tabulate"]
build-backend = "setuptools.build_meta"
EOF

sed -r -i "s/'pandoc', //" setup.py
sed -r -i "s/(TESTS_REQUIRE = \[.*)\]/\1, 'wrapt'\]/" setup.py

mv -i -v pytest_steps/tests/conftest.py .

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install

%check
args=(
  --ignore pytest_steps/tests/test_with_cases.py # avoid circular dep
)
PYTHONPATH=%{buildroot}/%{python3_sitelib} %{__python3} -m pytest -v "${args[@]}"

%files -n python3-pytest-steps
%license LICENSE
%doc README.md
%{python3_sitelib}/pytest_steps/
%{python3_sitelib}/pytest_steps-%{version}.dist-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.2-2
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.7.2-1
- Update to latest version (#1795548)

* Sat Aug 10 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.6.2-1
- Initial packaging
