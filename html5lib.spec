Summary: HTML5 parsing library
%define snap 20100213
Name:		html5lib
Version:	0.11.%{snap}
Release:	1
License:	BSD-like
Group:		Development/Languages
Source0:	%{name}-%{snap}.tar.gz
# Source0-md5:	b8ddef8236806a0a6c43900e42c2e347
URL:		http://code.google.com/p/html5lib/
BuildRequires:	setup.rb
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML5 parsing library

%package -n ruby-html5lib
Summary: Ruby HTML5 parser
Group:	Development/Languages
%{?ruby_mod_ver_requires_eq}

%description -n ruby-html5lib
Ruby port of the HTML5 parser


%prep
%setup -q -n %{name}

%build
cd ruby
cp /usr/share/setup.rb .
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}
ruby setup.rb setup
rdoc --ri --op ri lib
rdoc --op ../rdoc lib

%install
cd ruby
rm -rf $RPM_BUILD_ROOT
ruby setup.rb install --prefix=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%files -n ruby-html5lib
%doc rdoc
%attr(755,root,root) /usr/bin/html5
%{ruby_rubylibdir}/*
%{ruby_ridir}/HTML5
%{ruby_ridir}/HTMLConformanceChecker
