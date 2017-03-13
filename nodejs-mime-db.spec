%{?scl:%scl_package nodejs-mime-db}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global packagename mime-db
%global enable_tests 0

Name:		%{?scl_prefix}nodejs-mime-db
Version:	1.22.0
Release:	2%{?dist}
Summary:	This is a database of all mime types

License:	MIT
URL:		https://github.com/jshttp/mime-db
Source0:	https://github.com/jshttp/mime-db/archive/v%{version}.tar.gz

ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	%{?scl_prefix}nodejs-devel
%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}mocha
%endif

Requires:	%{?scl_prefix}nodejs

%description
This is a database of all mime types. It consists of a single, public JSON
file and does not include any logic, allowing it to remain as un-opinionated
as possible with an API. It aggregates data from the following sources:

 * http://www.iana.org/assignments/media-types/media-types.xhtml
 * http://svn.apache.org/repos/asf/httpd/httpd/trunk/docs/conf/mime.types
 * http://hg.nginx.org/nginx/raw-file/default/conf/mime.types

%prep
%setup -q -n %{packagename}-%{version}

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js db.json src/ scripts/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
#%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
/usr/bin/mocha -R spec
%endif

%files
%{!?_licensedir:%global license %doc}
%doc README.md HISTORY.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Sep 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.22.0-2
- Built for RHSCL

* Tue Feb 16 2016 Jared Smith <jsmith@fedoraproject.org> - 1.22.0-1
- Update to upstream 1.22.0 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 09 2016 Jared Smith <jsmith@fedoraproject.org> - 1.21.0-1
- Update to upstream 1.21.0 release

* Fri Nov 13 2015 Jared Smith <jsmith@fedoraproject.org> - 1.20.0-1
- Update to upstream 1.20.0 release

* Thu Oct 22 2015 Jared Smith <jsmith@fedoraproject.org> - 1.19.0-2
- Fix %license macro for EPEL6

* Wed Oct  7 2015 Jared Smith <jsmith@fedoraproject.org> - 1.19.0-1
- Initial packaging
